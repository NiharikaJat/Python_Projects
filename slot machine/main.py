import random

MAX_shares=3
MAX_AMOUNT=1000000
MIN_AMOUNT=10

ROWS=3
COLS=3

symbol_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}

symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

def check_winnings(columns,shares,invest,values):
    winnings=0
    winning_shares=[]
    for share in range(shares):
        symbol=columns[0][share]
        for column in columns:
            symbol_to_check=column[share]
            if symbol!=symbol_to_check:
                break 
        else:
            winnings+=values[symbol]*invest
            winning_shares.append(share+1)

    return winnings,winning_shares

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,count in symbols.items():
        for i in range(count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(COLS):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(ROWS):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i!=len(columns)-1:
                print(col[row],end=" | ")
            else:
                print(col[row])


def deposit():
    while True:
        amount=input("What would you like to deposit? Rs")
        if amount.isdigit():
            amount= int(amount)
            if amount>0:
                 break 
            else:
                print("Invalid amount!")
        else:
            print("Enter a number")
        
    return amount


def get_number_of_shares():
    while True:
        shares=input("Enter the number of shares you want to invest on (1-"+str(MAX_shares)+")? ")
        if shares.isdigit():
            shares=int(shares)
            if 1<=shares<=MAX_shares:
                 break 
            else:
                print("Invalid number!")
        else:
            print("Enter a number")
        
    return shares


def get_share():
    while True:
        amount=input("What would you like to invest on each share? Rs")
        if amount.isdigit():
            amount=int(amount)
            if MIN_AMOUNT<amount<MAX_AMOUNT:
                break 
            else:
                print(f"Amount must be between Rs{MIN_AMOUNT} - Rs{MAX_AMOUNT}!")
        else:
            print("Enter a number")
        
    return amount

def game(balance):
    shares=get_number_of_shares()
    while True:
        invest=get_share()
        total_invest=shares*invest 
        
        if total_invest>balance:
            print(f"You don't have enoough balance currently!")
        else:
            break

    print(f"You are investing Rs{invest} on Rs{shares} shares.Total invest is equal to: Rs{total_invest}")

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_share=check_winnings(slots,shares,invest,symbol_value)
    print(f"You got Rs{winnings}")
    print(f"You got on: ",*winning_share)

    return winnings-total_invest

def main():
    balance=deposit()
    while True:
        print(f"Current balance is Rs{balance}")
        answer=input("Press enter to continue(q to quit)")
        if answer.lower()=='q':
            break
        balance+=game(balance)

    print(f"You left with Rs{balance}")

main()