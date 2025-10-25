import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(os.name)
clear()