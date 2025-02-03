class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"{self.owner}'s Account Balance: {self.balance:.2f}")

owner_name = input("Name: ")
starting_balance = float(input("Enter starting balance: "))

account = Account(owner_name, starting_balance)

while True:
    action = input("\nDeposit, withdraw, balance, or exit: ").strip().lower()

    if action == "deposit":
        amount = float(input("Dposit amount: "))
        account.deposit(amount)
    elif action == "withdraw":
        amount = float(input("Withdrawal amount: "))
        account.withdraw(amount)
    elif action == "balance":
        account.display_balance()
    elif action == "exit":
        print("Exit")
        break
    else:
        print("Invalid action")
