import argparse
from typing import List,Dict,Any
from colorama import init,Fore,Style

def count(data: List[Dict[str,str]],to_count:str,to_match:str)->int:
    return sum(1 for line in data if line[to_count] == to_match)
     
def summary(data: List[Dict[str,str]],to_check: List[str]) -> Dict:
    dict_lvl = {}
    for i in to_check:
        dict_lvl[i] = 0
    for i in data:
        if i['level'] in to_check:
            dict_lvl[i['level']] += 1
    return dict_lvl

def main():
    init(autoreset= True)
    parser = argparse.ArgumentParser(description = 'Logparser tool')
    parser.add_argument('--file',type = str, help ='Path to the log file')
    parser.add_argument('--date',type = str, help = "Display logs based on date ")
    parser.add_argument('--level',type = str, help = 'The level for filter')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('--count',action = 'store_true', help = 'Gives the count for filters used')
    group.add_argument('--summary',action = 'store_true', help = 'Gives the summary of all the parameters in filter')

    args = parser.parse_args()
    line_ls = []
    pr_ls = []
    level_type = []
    with open(args.file,'r') as f:
        for line in f:
            line = line.strip()
            pr_ls.append(line)
            line_element = line.split()
            date = line_element[0].strip()
            time = line_element[1]
            level = line_element[2].strip().upper()

            if level not in level_type:
                level_type.append(level)
            message = ' '.join(line_element[3:])
            line_ls.append({"date": date,"time": time, "level": level, "message": message})
    if args.count:
        if args.date and args.level:
            filtered = [
    line for line in line_ls
    if line["date"].strip() == args.date.strip() and line["level"].strip().upper() == args.level.strip().upper()
]
            print('Found', Fore.RED + Style.BRIGHT + str(len(filtered)), 'matching lines.')
        elif args.date:
            print('Found', Fore.RED + Style.BRIGHT + str(count(line_ls, "date", args.date)), 'matching lines.')
        elif args.level:
            print('Found', Fore.RED + Style.BRIGHT + str(count(line_ls, "level", args.level)), 'matching lines.')
        else:
            print(Fore.YELLOW + " Please use --date and/or --level with --count.")
        return
    if args.date and args.summary:
        t = []
        for line in line_ls:
            if line['date'] ==  args.date:
                t.append(line)
        sry_dict = summary(t,level_type)
        for i,j in sry_dict.items():
            print(f'{i}: {j}')
        return 
    elif args.date:            
        for n,line in enumerate(line_ls):
            if line['date'] == args.date:
                print(pr_ls[n])    
    if args.level:
        for n, line in enumerate(line_ls):
            if line["level"] == args.level:
                print(pr_ls[n])
    
if __name__ == "__main__":
    main()
