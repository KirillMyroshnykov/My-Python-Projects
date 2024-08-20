# Python Slot Machine
import random
import time

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    results = [random.choice(symbols) for _ in range(3)]
    return results

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    print("**************************")
    print("Welcome to Python Slots!!!")
    print("**************************")

    while True:
        balance = input("How much money would you like to spend?: ")

        if not balance.isdigit():
            print("Please enter a valid INTEGER NUMBER!")
            continue
        else:
            balance = int(balance)
            break

    while balance > 0:
        print(f"Your current balance: ${balance}")

        bet = input("Place your bet: ")

        if not bet.isdigit():
            print("Please enter a valid INTEGER NUMBER!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds on your balance!")
            continue

        if bet <= 0:
            print('Bet must be greater than zero!')
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(2)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round")

        balance += payout

        play_again = input("Do you want to play again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("**********************************************")
    print(f"Game over! Your current balance is ${balance}")
    print("**********************************************")

main()