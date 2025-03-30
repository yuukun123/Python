class BankAccount:
    def __init__(self, accountNumber, accountName):
        self.accountName = accountName
        self.accountNumber = accountNumber
        self.balance = 0

    def getAccountName(self):
        return self.accountName

    def getAccountNumber(self):
        return self.accountNumber

    def getBalance(self):
        return self.balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.accountNumber}. New balance is {self.balance}")
        return self.balance

    def withdraw(self, amount):
        yes = True
        if amount > self.balance:
            yes = False
            return yes
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.accountNumber}. New balance is {self.balance}")
            return yes

    def __str__(self):
        return f"Account Name: {self.accountName}, Account Number: {self.accountNumber}, Balance: {self.balance}"