import random
import string

class BankAccount():

    def __init__ (self, name = 'username', balance = 0):

        self.name = name
        self.balance = balance
    
    def acc_no(self):
        
        def randStr(chars = string.ascii_uppercase + string.digits, n=8):
            num = ''
            num = num.join(random.choice(chars) for _ in range(n))
            return num
        number = randStr()
        
        return f'Dear {self.name}, your Account Number is: {self.number}.'

    def deposit (self, amount):
        
        self.balance += amount
        
        return f'Hey {self.name}, you have deposited KES. {self.balance} and your account now has KES. {self.balance}'
    
    def withdraw (self, amount):
        
        self.balance -= amount
        
        return f'Hey {self.name}, you have withdrawn KES. {amount} and your account now has KES. {self.balance}'
    def __str__(self):
        return f'Account Number: {self.number}\nAccount Holder: {self.name}\nAccount Balance: {self.amount}'
    
