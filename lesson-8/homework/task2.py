import json
import os
import uuid
from datetime import datetime


class Account:
    def __init__(self, account_number, name, balance=0.0, transactions=None):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((datetime.now().isoformat(), "Deposit", amount))
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.now().isoformat(), "Withdraw", amount))
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance,
                "transactions": self.transactions}


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def generate_account_number(self):
        return str(uuid.uuid4().int)[:10]

    def create_account(self, name, initial_deposit=0.0):
        account_number = self.generate_account_number()

        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance:.2f}")
            print("Transaction History:")
            for transaction in account.transactions:
                print(f"{transaction[0]} - {transaction[1]}: ${transaction[2]:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            try:
                amount = float(amount)
                if amount <= 0:
                    raise ValueError("Deposit must be greater than zero.")
                account.deposit(amount)
                self.save_to_file()
            except ValueError as e:
                print("Error:", e)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            try:
                amount = float(amount)
                if amount <= 0:
                    raise ValueError("Withdrawal amount must be positive.")
                account.withdraw(amount)
                self.save_to_file()
            except ValueError as e:
                print("Error:", e)
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
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, initial_deposit)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = input("Enter deposit amount: ")
            bank.deposit(acc_num, amount)
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = input("Enter withdrawal amount: ")
            bank.withdraw(acc_num, amount)
        elif choice == "5":
            print("Exiting Bank Application.")
            exit()
        else:
            print("Invalid choice. Please try again.")