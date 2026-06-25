# Banking System Project

accounts = {
    "1001": {"pin": "1234", "balance": 5000},
    "1002": {"pin": "5678", "balance": 3000},
    "1003": {"pin": "9999", "balance": 10000}
}


def login():
    accn = input("Enter the account number: ")
    pin = input("Enter the PIN number: ")

    if accn in accounts and accounts[accn]["pin"] == pin:
        print("Login Successful!")
        return accn
    else:
        print("Invalid account number or PIN!")
        return None


def deposit(accn):
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
    else:
        accounts[accn]["balance"] += amount
        print("Deposit Successful!")
        print(f"Current Balance: ₹{accounts[accn]['balance']:.2f}")


def withdraw(accn):
    amount = float(input("Enter the withdrawal amount: "))

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
    elif amount > accounts[accn]["balance"]:
        print("Insufficient Balance!")
    else:
        accounts[accn]["balance"] -= amount
        print("Withdrawal Successful!")
        print(f"Remaining Balance: ₹{accounts[accn]['balance']:.2f}")


def check_balance(accn):
    print(f"Current Balance: {accounts[accn]['balance']:.2f}")



user = login()

if user:
    while True:
        print("\n Banking Menu ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            deposit(user)

        elif choice == "2":
            withdraw(user)

        elif choice == "3":
            check_balance(user)

        elif choice == "4":
            print("Thank you for using our Banking System.")
            break

        else:
            print("Invalid choice! Please try again.")
