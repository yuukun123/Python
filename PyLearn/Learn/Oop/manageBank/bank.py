from BankAccount import BankAccount
import random

class bank:
    def __init__(self):
        self.bankAccount = []

    def addAccount(self, accountNumber, accountName):
        # accountNumber = input("Enter account number: ")
        # accountName = input("Enter account name: ")
        if accountNumber in self.bankAccount:
            print(False)
            print("Account already exists")
        else:
            newAccount = BankAccount(accountNumber, accountName)
            print(True)
            self.bankAccount.append(newAccount)
            print("Account created successfully\n")

    def generateRandomBalances(self):
        for account in self.bankAccount:
            random_balance = random.randint(0, 10000)  # Số tiền ngẫu nhiên từ 0 đến 10,000
            account.balance = random_balance  # Gán số dư ngẫu nhiên cho tài khoản
            print(f"Tài khoản {account.getAccountNumber()} có số dư: {random_balance}")

    def getItem(self, accountNumber):
        for account in self.bankAccount:
            acc_num = account.getAccountNumber()
            if acc_num == accountNumber:
                print("Match found!")  # Debug
                return account
        print("No match found.")  # Debug
        return None

    def getTotal(self):
        return len(self.bankAccount)

    def search(self, accountNumber):
        for index,account in enumerate(self.bankAccount):
            acc_num = account.getAccountNumber()
            if acc_num == accountNumber:
                return index
        return -1

    def depositMoney(self, accountNumber, money):
        for index,account in enumerate(self.bankAccount):
            acc_num = account.getAccountNumber()
            if acc_num == accountNumber:
                return account.deposit(money)
        return -1

    def withdrawMoney(self, accountNumber, money):
        for index,account in enumerate(self.bankAccount):
            acc_num = account.getAccountNumber()
            if acc_num == accountNumber:
                return account.withdraw(money)
        return -1

    def removeAccount(self, accountNumber):
        for index,account in enumerate(self.bankAccount):
            acc_num = account.getAccountNumber()
            if acc_num == accountNumber:
                self.bankAccount.pop(index)
                return True
        return False

    def displayTransactionStatus(self):
        if not self.bankAccount:
            print("No accounts found.")
            return
        else:
            print("report transaction status")
            for account in self.bankAccount:
                print(f"Tài khoản {account.getAccountNumber()} - Số dư: {account.getBalance()}")


    def display(self):
        if not self.bankAccount:
            print("No accounts found.")
        else:
            for account in self.bankAccount:
                print(account.getAccountName(), account.getAccountNumber(), account.getBalance())



