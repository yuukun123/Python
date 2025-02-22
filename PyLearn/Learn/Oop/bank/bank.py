class bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, account_number, initial_balance = 0):
        if account_number in self.customers:
            print("Account already exists")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully")

    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful")
        else:
            print("Account does not exist")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
            else:
                print("insufficent funds")
        else:
            print("account number does not exist")

    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"account balance: {balance}")
        else:
            print("account number does not exist")