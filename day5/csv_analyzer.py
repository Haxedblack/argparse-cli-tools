import argparse
import sys
import csv
from statistics import mean,median,stdev
from colorama import init, Fore, Style
init(autoreset = True)
def compute_stats(values, stats):
    result = {}
    if not values:
        result = {stat: 'N/A' for stat in stats}
    if 'mean' in stats:
        result['mean'] = mean(values)
    if 'median' in stats:
        result['median'] = median(values)
    if 'std' in stats and len(values) > 1:
        result['std']= stdev(values)
    if 'min' in stats:
        result['min'] = min(values)
    if 'max' in stats:
        result['max'] = max(values)

    return result


def read_csv(file_path):
    try:
        with open(file_path,'r',newline = '') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            return rows
    except FileNotFoundError:
        print(f'File not found at {file_path}')
        sys.exit(1)
    except Exception as e:
        print(f'Problem reading CSV: {e}')
        sys.exit(1)
def main():
    parser = argparse.ArgumentParser(description='CSV Analyzer')
    parser.add_argument('--file',required = True , help = 'Path to the csv file')
    parser.add_argument('--columns',type = str , help = 'Columns separated by comma')
    parser.add_argument('--stats',type = str , help = 'Stats to show')
    parser.add_argument('--head',type = int ,help= "Number of rows to show")

    args = parser.parse_args()

    print("File to read: ", args.file)
    print('Columns to analyze: ' , args.columns)
    print('Stats to analyze:' , args.stats)
    print('Preview Head: ', args.head)
    
    rows = read_csv(args.file)
    if args.head:
        print(f'\n Showing first {args.head} rows:\n')
        for i, row in enumerate(rows[:args.head], 1):
            print(f"{i:>2}. " + ", ".join(f"{k}={v}" for k, v in row.items()))

    valid_st = {'mean','median','std','min','max'}
    if args.stats:
        stats = {stat.strip() for stat in args.stats.split(',')}
        invalid = stats - valid_st
        if invalid:
            print(f'Invalid stat: {invalid}')
            sys.exit(1)
    else:
        stats = valid_st
        
    if not args.columns:
        print(" No --columns specified, auto-detecting numeric columns.")
        sample_row = rows[0]
        column = [k for k, v in sample_row.items() if v.replace('.', '', 1).isdigit()]
    else:
        column = [col.strip() for col in args.columns.split(',')]
    header = rows[0].keys()
    for col in column:
        if col not in header:
            print(f"Column '{col}' not found in file.")
            sys.exit(1)
    print(Style.BRIGHT + Fore.CYAN + f"\n Analyzing columns: {', '.join(column)}\n")
    for col in column:
        try:
            values = [float(row[col]) for row in rows if row[col] != '']
            stat_result = compute_stats(values,stats)
            print(Fore.GREEN +f"-> {col}")
            for stat, value in stat_result.items():
                print(Fore.YELLOW + f"  {stat.capitalize()}: {value:.2f}" if isinstance(value, float) else f"  {stat.capitalize()}: {value}")
        except ValueError:
            print(f" Skipping column '{col}': contains non-numeric values.")
if __name__=='__main__':
    main()