# 📈 Stock-Fetch CLI (Day 7)

A command-line tool to fetch real-time stock data using the Alpha Vantage API.

This project introduces using the `requests` library to interact with external APIs, handling secret keys (API keys), and parsing JSON responses.

---

## 🚀 Features

- 💵 Fetches real-time stock quotes.
- 🔑 Securely handles API keys via command-line argument or environment variable.
- 📉 Parses API JSON responses.
- 🎨 Colored and formatted output for readability.
- 🛡️ Robust error handling for network or API issues.

---

## 🛠️ Setup

1.  **Install `requests`**:
    ```bash
    pip install requests
    ```

2.  **Get a Free API Key**:
    -   Go to [Alpha Vantage](https://www.alphavantage.co/) and get your free API key.

3.  **Set Environment Variable (Recommended)**:
    -   This is the best way to keep your key secret.
    ```bash
    export ALPHA_VANTAGE_KEY="YOUR_API_KEY_HERE"
    ```
    -   (You can add this line to your `.bashrc` or `.zshrc` to make it permanent)

---

## 🧪 Example Usage

### ✅ Get a full quote (default)

```bash
# Assumes you set the environment variable
python day7/stock.py GOOG