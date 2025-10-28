from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance 

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}, New balance: {self._balance}")

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}, Remaining: {self._balance}")

acc = SavingsAccount("Saqib", 1000)
acc.deposit(500)
acc.withdraw(300)
