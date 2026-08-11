class BankAccount:
    def __init__(self, name):
        self.name = name
        self._balance = 0
    def deposit(self, amount):
        self._balance = self._balance + amount
    def withdraw(self, amount):
        self._balance = self._balance - amount
    def transfer(self, amount, recipient):
        self.withdraw(amount)
        recipient.deposit(amount)
    def __str__(self):
        return "Account " + self.name + " has balance $" + str(self._balance)