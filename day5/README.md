# 📊 CSV Column Analyzer (Day 5)

A lightweight command-line tool that analyzes numeric columns in a `.csv` file and computes user-specified statistics like mean, standard deviation, median, min, and max.

---

## 🚀 Features

- 📁 Read CSV files using `csv.DictReader`
- 📊 Analyze specific columns via `--columns`
- 🧠 Compute column-wise statistics:
  - `mean`, `std`, `median`, `min`, `max`
- 🔍 Preview first N rows with `--head`
- 🔒 Graceful error handling for missing files/columns
- 🎨 Colored CLI output using `colorama`

---

## 🧪 Example Usage

```bash
python day5/csv_analyzer.py \
  --file data/sample.csv \
  --columns price,volume \
  --stats mean,std \
  --head 3
```
## 📤 Sample Output
```
File to read:  data/sample.csv
Columns to analyze:  price,volume
Stats to analyze: mean,std
Preview Head:  3

 Showing first 3 rows:

 1. symbol=AAPL, price=101.2, volume=15000
 2. symbol=AAPL, price=102.5, volume=15200
 3. symbol=AAPL, price=100.9, volume=14800

 Analyzing columns: price, volume

→ price
   Mean      : 904.46
   Std       : 1245.04

→ volume
   Mean      : 9900.00
   Std       : 5265.61
```
## 📁 Folder Structure
```
argparse-cli-tools/
├── day5/
│   ├── csv_analyzer.py
│   └── README.md
├── data/
│   └── sample.csv
```