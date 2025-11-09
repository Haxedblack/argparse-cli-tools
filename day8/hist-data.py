import argparse
import requests
import os
import sys
import csv
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="Fetches historical stock data and saves it as a CSV.")
    
    parser.add_argument("symbol", 
                        type=str, 
                        help="The stock ticker symbol (e.g., AAPL)")
                        
    parser.add_argument("--output", 
                        type=str, 
                        help="Output CSV file name (default: [symbol]_data.csv)")
    
    parser.add_argument("--api-key", 
                        type=str, 
                        help="Your Alpha Vantage API key (better: set ALPHA_VANTAGE_KEY env var)")

    parser.add_argument("--full", 
                        action="store_true", 
                        help="Fetch the full 20+ years of data (default: 100 days)")