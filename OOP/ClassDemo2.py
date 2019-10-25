class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0.0
        
    def deposit(self,num):
        self.balance += num
        return self.balance
        
    def withdraw(self,num):
        self.balance -= num
        return self.balance
        
#This is implemetation of Class BankAccount in ClassDemo2.py
acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
acct.deposit(10)
acct.withdraw(3)
print(acct.balance)