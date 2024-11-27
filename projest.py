# ATM Simulator

# Dummy data for a single account
account = {
    "pin": "1234",
    "balance": 5000.0
}

def main_menu():
    print("\n=== ATM Simulator ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def check_balance():
    print(f"\nYour current balance is: ${account['balance']}")

def deposit_money():
    amount = float(input("\nEnter the amount to deposit: "))
    if amount > 0:
        account['balance'] += amount
        print(f"${amount} deposited successfully!")
    else:
        print("Invalid amount entered.")

def withdraw_money():
    amount = float(input("\nEnter the amount to withdraw: "))
    if 0 < amount <= account['balance']:
        account['balance'] -= amount
        print(f"${amount} withdrawn successfully!")
    elif amount > account['balance']:
        print("Insufficient funds!")
    else:
        print("Invalid amount entered.")

def atm_simulator():
    # Authenticate user
    pin = input("Enter your PIN: ")
    if pin == account["pin"]:
        print("\nAuthentication Successful!")
        while True:
            choice = main_menu()
            if choice == "1":
                check_balance()
            elif choice == "2":
                deposit_money()
            elif choice == "3":
                withdraw_money()
            elif choice == "4":
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
    else:
        print("\nIncorrect PIN. Access denied!")

# Run the ATM simulator
atm_simulator()
