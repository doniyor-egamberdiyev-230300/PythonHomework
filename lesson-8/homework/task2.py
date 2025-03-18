import json
import os


class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit=0.0):
        account_number = str(len(self.accounts) + 1000)
        if account_number in self.accounts:
            print("Account number already exists. Try again.")
            return

        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, file)

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {acc: Account(**data[acc]) for acc in data}


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)
        elif choice == "5":
            print("Exiting Bank Application.")
            exit()
        else:
            print("Invalid choice. Please try again.")