import argparse
import time
def main():
    parser = argparse.ArgumentParser(description = "Simple Countdown Timer")
    group = parser.add_mutually_exclusive_group(required="True")
    group.add_argument('--minutes', type = int , help = 'Countdown in minutes')
    group.add_argument('--seconds',type = int, help = 'Countdown in seconds')
    
    parser.add_argument('--message', type = str, help = 'Message to display when timer is over')
    parser.add_argument('--verbose',action = 'store_true')
    args = parser.parse_args()
    total_seconds = 0
    if args.minutes:
        total_seconds = args.minutes * 60
    elif args.seconds:
        total_seconds = args.seconds
    
    if total_seconds <= 0:
        print("Please provide positive time duration.")
        return
    if args.verbose:
        print(f'Starting timer for {total_seconds} seconds...')
    for remaining in range(total_seconds,0 , -1):
        mins , secs = divmod(remaining , 60)
        time_r = f"  Time Left: {mins:02d}:{secs:02d}"
        #to print on the same line overwriting
        print("\r",time_r,end='', flush = True)
        time.sleep(1)
    if args.verbose:
        print(" Time's up!")
    if args.message:
        print(args.message)
    

if __name__ == '__main__':
    main()
