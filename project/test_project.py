import numpy as np
import pytest

from project import (
    calculate_risk_contribution,
    calculate_market_impact,
    rebalance_to_equal_risk,
    calculate_max_drawdown,
    load_portfolio,
    STOCK_MAP,
)


def test_calculate_risk_contribution():
    cov = np.array([
        [0.04, 0.0],
        [0.0,  0.01]
    ])
    w = np.array([0.5, 0.5])
    rc = calculate_risk_contribution(w, cov)
    assert np.allclose(rc, [80.0, 20.0], atol=1e-5)
    assert np.isclose(np.sum(rc), 100.0)

    rc_pct = calculate_risk_contribution(np.array([50.0, 50.0]), cov)
    assert np.allclose(rc_pct, [80.0, 20.0], atol=1e-5)

    with pytest.raises(ValueError):
        calculate_risk_contribution(np.array([0.5, 0.5]), np.eye(3))


def test_calculate_market_impact():
    slippage, days = calculate_market_impact(10000, 2000.0, 0.0644)
    assert days == 25.0
    assert slippage == 7.25

    slippage_std, days_std = calculate_market_impact(10000, 2000.0, 0.035)
    assert days_std == 25.0
    assert slippage_std == 3.96

    slip_small, days_small = calculate_market_impact(10, 100000.0, 0.02)
    assert days_small == 1.0
    assert slip_small >= 0.05

    slip_zero, days_zero = calculate_market_impact(0, 1000.0, 0.02)
    assert slip_zero == 0.0
    assert days_zero == 0.0

    with pytest.raises(ValueError):
        calculate_market_impact(-5, 1000.0, 0.02)
    with pytest.raises(ValueError):
        calculate_market_impact(100, 0.0, 0.02)
    with pytest.raises(ValueError):
        calculate_market_impact(100, 1000.0, -0.01)


def test_rebalance_to_equal_risk():
    # stock with RC 60% (too high) must lose weight, stock with RC 10% must gain weight
    test_weights = np.array([0.5, 0.3, 0.2])
    test_rc = np.array([60.0, 30.0, 10.0])
    w_new = rebalance_to_equal_risk(test_rc, test_weights)

    assert len(w_new) == 3
    assert np.isclose(np.sum(w_new), 1.0)
    assert w_new[0] < test_weights[0]   # over-risk stock loses weight
    assert w_new[2] > test_weights[2]   # under-risk stock gains weight

    # equal RC -> weights stay the same after normalization
    eq_weights = np.array([1/3, 1/3, 1/3])
    eq_rc = np.array([33.33, 33.33, 33.34])
    w_eq = rebalance_to_equal_risk(eq_rc, eq_weights)
    assert np.allclose(w_eq, [1/3, 1/3, 1/3], atol=0.01)

    with pytest.raises(ValueError):
        rebalance_to_equal_risk(np.array([]), np.array([]))
    with pytest.raises(ValueError):
        rebalance_to_equal_risk(np.array([0.0, 20.0, 80.0]), np.array([0.33, 0.33, 0.34]))


def test_calculate_max_drawdown():
    prices = [100.0, 120.0, 90.0, 110.0]
    assert calculate_max_drawdown(prices) == -25.0
    assert calculate_max_drawdown([10.0, 20.0, 30.0]) == 0.0
    assert calculate_max_drawdown([50.0]) == 0.0


def test_load_portfolio(tmp_path):
    test_file = tmp_path / "test_portfolio.csv"
    test_file.write_text("Stock names,No. of shares holds\ntesla,6\nmicrosoft,15\nreliance,20\n", encoding="utf-8")
    names, tickers, shares = load_portfolio(str(test_file))
    assert names == ["tesla", "microsoft", "reliance"]
    assert tickers == ["TSLA", "MSFT", "RELIANCE.NS"]
    assert shares == [6, 15, 20]

    names_p, tickers_p, shares_p = load_portfolio("portfolio.csv")
    assert len(names_p) > 0
    assert len(tickers_p) == len(names_p)
    assert len(shares_p) == len(names_p)
