import random



MAX_LINES = 5
MAX_DEP = 100
MAX_BET = 50

ROWS = 5
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


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
                print("Enter a valid number of lines!")
        else:
            print("Has to be a whole number dude!")
    return lines

def get_bet():
    while True:
        amount = input(f"How much would you like to bet on each line between 1 and {MAX_BET}? $")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_BET:
                break
            else:
                print(f"Enter a valid bet between 1 and {MAX_BET} total!")
        else:
            print("Has to be a whole number dude!")
    return amount


def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough money! Your current balance is ${balance}.")
        else:
            break
    print(f"You are all set for ${bet} on {lines} lines. All in for ${total_bet}. Good Luck!")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()