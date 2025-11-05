import argparse
import requests
import json 
import os
from colorma import init, Fore

init(autoreset=True)

def main():
    parser= argparse.ArgumentParser(description="Fetches stock data from API.")
    parser.add_argument("symbol", type = str , help = "Stock Symbols eg: AAPL")
    parser.add_argument('--api-key', type = str, help = "Your Alpha Advantage API Key")
    parser.add_argument('--info', type = str, choices = ['prices','quote'], default = 'quote', help = "What info to fetch (default: quote)")

    args=parser.parse_args()

    print(f"Fetching {args.info} for {args.symbol}...")
    