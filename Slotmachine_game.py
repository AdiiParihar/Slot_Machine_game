import random
L = ['🍒', '🍋', '🍉', '💎', '🔔']
wallet = 0
def game():
    a = []
    for _ in range(3):
        a.append(random.choice(L))
    print(" Spin result: ", ' | '.join(a))
    if a[0] == a[1] == a[2]:
        return 2  # Jackpot
    elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        return 1
    else:
        return 0
def transaction(amount, mode):
    global wallet
    if mode == 0:
        wallet += amount
        print(f" Deposited ₹{amount}. New balance: ₹{wallet}")
    elif mode == 1:
        if wallet >= amount:
            wallet -= amount
            print(f" Bet of ₹{amount} placed. Remaining balance: ₹{wallet}")
            return True
        else:
            print(" Insufficient balance.")
            return False

print("-----------🎰 WELCOME TO SLOT MACHINE 🎰------------")

while True:
    print("\nWhat do you want to do?")
    print("1. Deposit ")
    print("2. Withdrawal ")
    print("3. Check Balance ")
    print("4. Play Game ")
    print("5. Exit ")

    try:
        n = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match n:
        case 1:
            amt = int(input("Enter amount to deposit: ₹"))
            transaction(amt, 0)

        case 2:
            amt = int(input("Enter amount to withdraw: ₹"))
            transaction(amt, 1)

        case 3:
            print(f" Wallet balance: ₹{wallet}")

        case 4:
            while True:
                try:
                    bet = int(input("Place your bet: ₹"))
                except ValueError:
                    print("Invalid input.")
                    continue
                if transaction(bet, 1):
                    result = game()
                    if result == 2:
                        print(" JACKPOT! Your amount is quadrupled!")
                        transaction(bet * 4, 0)
                    elif result == 1:
                        print(" You won! Your amount is doubled!")
                        transaction(bet * 2, 0)
                    else:
                        print(" You lost this round.")

                again = input("Play again? (y/n): ").lower()
                if again == 'n':
                    print("Thanks for playing ")
                    break

        case 5:
            print("Goodbye! ")
            break

        case _:
            print("Invalid choice. Try again.")