class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} dollars.")
        else:
            raise ValueError("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} dollars.")
        else:
            raise ValueError("Withdrawal amount must be greater than zero and less than or equal to the balance.")

try:
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)  # This will raise an exception
except ValueError as e:
    print("Error:", e)
