
import argparse
import requests
import json
import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def fetch_data(symbol, api_key, info):
    # Try to get the API key from the argument,
    # if not, fall back to an environment variable
    key = api_key or os.getenv("ALPHA_VANTAGE_KEY")
    
    if not key:
        print(Fore.RED + "Error: API key not provided.")
        print("Please use --api-key or set the ALPHA_VANTAGE_KEY environment variable.")
        sys.exit(1)

    # We'll use the GLOBAL_QUOTE function from Alpha Vantage
    BASE_URL = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": key
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # Raises an error for bad responses (4xx or 5xx)
    
        data = response.json()
        
        # Check if the API returned an error (e.g., invalid symbol)
        if "Error Message" in data:
            print(Fore.RED + f"API Error: {data['Error Message']}")
            sys.exit(1)
        
        quote = data.get("Global Quote")
        
        if not quote or not quote.get('05. price'):
            print(Fore.RED + f"Could not find quote data for '{symbol}'.")
            print(Fore.YELLOW + "Note: The free API is limited to 25 requests/day.")
            sys.exit(1)

        # Now, print the requested info
        if info == "price":
            print(f"{Fore.CYAN}{symbol} Price: {Style.BRIGHT}{quote['05. price']}")
        
        elif info == "quote":
            print(f"{Style.BRIGHT}--- Quote for {Fore.CYAN}{symbol} ---")
            print(f"  Price:     {Fore.GREEN}{quote['05. price']}")
            print(f"  Open:      {quote['02. open']}")
            print(f"  High:      {quote['03. high']}")
            print(f"  Low:       {quote['04. low']}")
            print(f"  Volume:    {quote['06. volume']}")
            print(f"  Prev. Close: {quote['08. previous close']}")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Network or HTTP Error: {e}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(Fore.RED + "Error: Failed to parse API response (JSON).")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Fetches stock data from an API.")
    
    parser.add_argument("symbol", 
                        type=str, 
                        help="The stock ticker symbol (e.g., AAPL, GOOG)")
                        
    parser.add_argument("--api-key", 
                        type=str, 
                        help="Your Alpha Vantage API key (better: set ALPHA_VANTAGE_KEY env var)")

    parser.add_argument("--info", 
                        type=str, 
                        choices=["price", "quote"], 
                        default="quote", 
                        help="What information to fetch (default: quote)")
    
    args = parser.parse_args()

    fetch_data(args.symbol, args.api-key, args.info)


if __name__ == "__main__":
    main()
