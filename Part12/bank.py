# Name Isam Zia Roll no: TRN-2026-00346


class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Starting balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"{self.owner}: {self.balance}"
