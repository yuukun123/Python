from bank import bank

class menuBank:
    def menu(self):
        bank1 = bank()

        accNumber1 = "SB-123"
        accName1 = "yuu"

        accNumber2 = "SB-124"
        accName2 = "min"

        accNumber3 = "SB-125"
        accName3 = "soo"


        bank1.addAccount(accNumber1, accName1)
        bank1.addAccount(accNumber2, accName2)
        bank1.addAccount(accNumber3, accName3)
        bank1.generateRandomBalances()
        bank1.display()

        bank1.depositMoney(accNumber1, 50000000)
        bank1.withdrawMoney(accNumber1, 30000000)

        print("\nAfter transactions:")
        bank1.displayTransactionStatus()
        # bank1.display()
