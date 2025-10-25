# Timer which runs for a set limit
import os
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def counter(set_limit):
    count = 0
    try:
        while True:
            clear()
            mins, secs = divmod(count, 60)
            print(f"{mins:02}:{secs:02}", end="")
            sys.stdout.flush()
            time.sleep(1)
            count += 1
            if count > set_limit:
                print('\nTime Over...')
                break
    except KeyboardInterrupt:
        print('\nStopped.')

print("Enter the limit (seconds):")
set_limit = int(input('> '))
counter(set_limit)
