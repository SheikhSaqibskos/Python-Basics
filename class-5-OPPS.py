# Bank Account System using OOP concepts
# Author: Sheikh Saqib
# Description: Demonstrates Abstraction, Inheritance, Encapsulation, and Polymorphism in Python.

from abc import ABC, abstractmethod

# ----- Abstract Base Class -----
class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # Encapsulation (protected attribute)

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self._balance += amount
            print(f"Deposited: {amount}. New balance: {self._balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self._balance}")


# ----- Derived Class: Savings Account -----
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds! Cannot withdraw.")
        else:
            self._balance -= amount
            print(f"Withdrew: {amount}. Remaining balance: {self._balance}")


# ----- Derived Class: Current Account -----
class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            print("Transaction declined! Overdraft limit exceeded.")
        else:
            self._balance -= amount
            print(f"Withdrew: {amount}. Remaining balance: {self._balance}")


# ----- Bank Class (Manages multiple accounts) -----
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account added for {account.owner} in {self.name} bank.")

    def show_all_accounts(self):
        print(f"\n=== {self.name} Bank Accounts ===")
        for acc in self.accounts:
            acc.show_balance()


# ----- Main Program -----
if __name__ == "__main__":
    print("=== Welcome to the Python Bank System ===")

    bank = Bank("Vertex Bank")

    # Creating accounts
    acc1 = SavingsAccount("Saqib", 1000)
    acc2 = CurrentAccount("Ali", 2000, overdraft_limit=1000)

    # Adding accounts to the bank
    bank.add_account(acc1)
    bank.add_account(acc2)

    # Performing transactions
    acc1.deposit(500)
    acc1.withdraw(300)
    acc2.withdraw(2500)  # Uses overdraft

    # Show all account balances
    bank.show_all_accounts()
