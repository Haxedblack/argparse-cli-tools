# 💾 Historical Data Downloader (Day 8)

A CLI tool to fetch historical daily stock data from Alpha Vantage and save it as a `.csv` file.

This project combines the skills from Day 7 (API requests) and Day 5 (CSV handling). It shows how to use `requests` to fetch complex JSON data, parse it, and use the `csv` module to write it to a file.

---

## 🚀 Features

- 📈 Fetches daily time-series data (`open`, `high`, `low`, `close`, `volume`).
- 💾 Saves data in a clean `.csv` format, perfect for analysis.
- 📦 Supports "compact" (100 days) or "full" (20+ years) data fetching via a `--full` flag.
- Smart default file naming (e.g., `AAPL_data.csv`).
- 🔑 Securely handles API keys via argument or environment variable.

---

## 🛠️ Setup

(Requires `requests` and `colorama`)
```bash
pip install requests colorama