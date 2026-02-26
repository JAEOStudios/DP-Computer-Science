from B3BankAccount import BankAccount
joe = BankAccount("Joe")
joseph = BankAccount("Joseph")
jerome = BankAccount("Jerome")

joe.deposit(100)
joseph.deposit(200)
jerome.deposit(50000)

joe.withdraw(200)
joseph.withdraw(134)
jerome.transfer(4000, joe)

print(joe)
print(joseph)
print(jerome)
