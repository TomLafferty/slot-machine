import random


MAX_LINES = 5
MAX_DEP = 100
MIN_DEP = 1

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit more than zero!")
        else:
            print("Has to be a whole number dude.")
    return amount

def get_num_of_lines():
    while True:
        lines = input(f"Feeling lucky? Enter the number of lines to bet on between 1 and {MAX_LINES}: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines: ")
        else:
            print("Has to be a whole number dude: ")
    return lines

def main():
    balance = deposit()
    lines = get_num_of_lines()
    print(balance, lines)

main()