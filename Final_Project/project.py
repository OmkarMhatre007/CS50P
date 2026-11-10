import sys
import csv
import math
import numpy as np
import pandas as pd

STOCK_MAP = {
    'apple': 'AAPL',
    'nvidia': 'NVDA',
    'google': 'GOOGL',
    'alphabet': 'GOOGL',
    'tesla': 'TSLA',
    'microsoft': 'MSFT',
    'meta': 'META',
    'facebook': 'META',
    'amazon': 'AMZN',
    'samsung': '005930.KS',
    'reliance': 'RELIANCE.NS',
    'tata': 'TCS.NS',
    'tata motors': 'TATAMOTORS.NS',
    'tata steel': 'TATASTEEL.NS',
    'infosys': 'INFY.NS',
    'acer': '2353.TW',
    's&p 500': '^GSPC',
    'nifty 50': '^NSEI',
    'nifty': '^NSEI'
}


def calculate_risk_contribution(weights, cov_matrix):
    weights = np.array(weights, dtype=float)
    cov = np.array(cov_matrix, dtype=float)
    port_var = weights @ cov @ weights
    if port_var == 0:
        return np.zeros(len(weights))
    port_vol = math.sqrt(port_var)
    mrc = cov @ weights / port_vol
    return (weights * mrc / port_vol) * 100.0


def calculate_market_impact(shares_owned, adv, volatility):
    if shares_owned < 0:
        raise ValueError("Shares owned cannot be negative")
    if shares_owned == 0:
        return 0.0, 0.0
    if adv <= 0:
        raise ValueError("ADV must be positive")
    if volatility < 0:
        raise ValueError("Volatility cannot be negative")

    raw_days = shares_owned / (0.20 * adv)
    days_to_exit = max(1.0, raw_days)

    vol_pct = volatility * 100.0 if volatility <= 1.0 else volatility
    slippage_pct = 0.05 + 0.5 * vol_pct * math.sqrt(shares_owned / adv)

    return round(float(slippage_pct), 2), round(float(days_to_exit), 2)


def rebalance_to_equal_risk(risk_contributions, weights):
    if len(risk_contributions) == 0 or len(weights) == 0:
        raise ValueError("Inputs cannot be empty")
    target_rc = 100.0 / len(risk_contributions)
    adjusted = []
    for rc, w in zip(risk_contributions, weights):
        if rc <= 0:
            raise ValueError("Risk contributions must be positive")
        adjusted.append(w * (target_rc / rc))
    total = sum(adjusted)
    return np.array([a / total for a in adjusted], dtype=float)


def calculate_max_drawdown(prices):
    if len(prices) <= 1:
        return 0.0
    peak = prices[0]
    max_dd = 0.0
    for p in prices:
        if p > peak:
            peak = p
        dd = (p - peak) / peak
        if dd < max_dd:
            max_dd = dd
    return round(float(max_dd) * 100.0, 2)


def load_portfolio(filepath="portfolio.csv"):
    stock_names = []
    tickers = []
    shares = []
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if len(row) >= 2:
                name = row[0].strip().lower()
                qty = int(row[1].strip())
                if name in STOCK_MAP:
                    stock_names.append(name)
                    tickers.append(STOCK_MAP[name])
                    shares.append(qty)
                else:
                    print(f"Notice: '{row[0].strip()}' is not in the recognized stock list.")

    if not tickers:
        raise ValueError("No valid stocks found in portfolio file")

    return stock_names, tickers, shares


def load_data(tickers):
    try:
        import yfinance as yf
        print(f"Fetching live data for: {', '.join(tickers)}...")
        df = yf.download(tickers, period="60d", progress=False, timeout=5)
        if not df.empty and "Close" in df and "Volume" in df:
            close = df["Close"][tickers].ffill().bfill().round(2)
            volume = df["Volume"][tickers].ffill().bfill().astype(int)
            close.to_csv("live_prices.csv")
            volume.to_csv("live_volumes.csv")
            print("Loaded live data from Yahoo Finance.")
            return close, volume
    except Exception as e:
        print(f"Live fetch unavailable ({e}). Using offline data.")

    print("Loading offline data from prices.csv & volumes.csv...")
    close = pd.read_csv("prices.csv", index_col=0)[tickers]
    volume = pd.read_csv("volumes.csv", index_col=0)[tickers]
    return close, volume


def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "portfolio.csv"

    print("\n" + "=" * 65)
    print("               Portfolio Risk & Liquidity Diagnostic")
    print("=" * 65)

    try:
        stock_names, tickers, shares = load_portfolio(filepath)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        sys.exit(1)

    prices_df, volumes_df = load_data(tickers)
    n = len(tickers)

    latest_prices = [float(prices_df[t].iloc[-1]) for t in tickers]
    values = [s * p for s, p in zip(shares, latest_prices)]
    total_val = sum(values)
    weights = [v / total_val if total_val > 0 else 1.0 / n for v in values]

    prev = prices_df[tickers].shift(1)
    returns = ((prices_df[tickers] - prev) / prev).dropna()
    vols = returns.std().values
    cov = returns.cov().values

    rc = calculate_risk_contribution(weights, cov)
    rebal_w = rebalance_to_equal_risk(rc, weights)
    adv_vals = volumes_df[tickers].mean().values

    print("\n1. Weight vs True Risk Contribution:")
    print(f"{'Stock':<12} | {'Ticker':<12} | {'Weight %':<9} | {'Risk %':<9} | {'Note'}")
    print("-" * 65)
    for i in range(n):
        w_pct = weights[i] * 100
        diff = rc[i] - w_pct
        note = "High Risk Contributor" if diff >= 10 else ("Low Risk" if diff <= -5 else "Normal")
        print(f"{stock_names[i]:<12} | {tickers[i]:<12} | {w_pct:>8.1f}% | {rc[i]:>8.1f}% | {note}")

    top2 = sum(sorted(rc, reverse=True)[:2])
    if top2 >= 60.0:
        print(f"\nWarning: Top 2 stocks make up {top2:.1f}% of total portfolio risk!")
        print("High concentration significantly increases vulnerability to drawdowns.")

    print("\n2. Liquidity & Market Impact:")
    print(f"{'Ticker':<12} | {'Shares':<10} | {'ADV':<12} | {'Days to Exit':<12} | {'Slippage %'}")
    print("-" * 65)
    for i in range(n):
        slip, days = calculate_market_impact(shares[i], adv_vals[i], vols[i])
        print(f"{tickers[i]:<12} | {shares[i]:>10,d} | {adv_vals[i]:>12,.0f} | {days:>10.1f} d | {slip:>9.2f}%")

    print("\n3. Equal Risk Rebalance Suggestion:")
    print(f"{'Ticker':<12} | {'Current Wt %':<13} | {'Suggested Wt %':<15} | {'Daily Volatility'}")
    print("-" * 65)
    for i in range(n):
        print(f"{tickers[i]:<12} | {weights[i]*100:>11.1f}% | {rebal_w[i]*100:>13.1f}% | {vols[i]*100:>14.2f}%")

    port_sd = math.sqrt(np.array(weights) @ cov @ np.array(weights))
    print(f"\nPortfolio Volatility: {port_sd * 100:.2f}% daily ({port_sd * math.sqrt(252) * 100:.1f}% annualized)")
    print("\nHistorical 60-Day Max Drawdowns:")
    for t in tickers:
        mdd = calculate_max_drawdown(prices_df[t].values)
        print(f"  {t:<12}: {mdd:>6.2f}%")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
