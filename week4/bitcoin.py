import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=5dd8bb96bb77e4e7ca1074ad7dd8ea14e7721b6e6c077a1e3fffd2511273bb3e"
        
        answer = requests.get(url)
        answer.raise_for_status() 
        
        data = answer.json()
        price = float(data["data"]["priceUsd"])
        
    except (KeyError, ValueError):
        sys.exit("Error parsing data")

    total_cost = n * price
    print(f"${total_cost:,.4f}")

main()
