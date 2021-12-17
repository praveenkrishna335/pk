import sys
class customer:
    bank = "YES BANK"
    print("WELCOME TO {} ONLINE BANKING SYSTEM".format(bank))
    def __init__(self,name,acc,balance = 500):
        self.name = name
        self.acc = acc
        self.balance = balance
        print("Your balance is : ", self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Your balance after deposit is : ", self.balance)

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print("Your balance after withdraw is : ", self.balance)

name = input("Enter customer name : ")
account_no = int(input("Enter account no : "))
customer1 = customer(name,account_no)

while True:
    print("D - DEPOSIT\nW - WITHDRAW\nS - STOP")
    choice = input("Enter your choice : ")
    if choice == 'D':
        amount = int(input("Enter deposit amount : "))
        customer1.deposit(amount)
    elif choice == 'W':
        amount = int(input("Enter withdraw amount : "))
        customer1.withdraw(amount)
    else:
        sys.exit()