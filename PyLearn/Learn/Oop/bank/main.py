from bank import bank

if __name__ == "__main__":
    bank = bank()

    acno1 = "SB-123"
    damt1 = 1000
    print("New a/c No.: ", acno1, "Deposit Amount:", damt1)
    bank.create_account(acno1, damt1)

    acno2 = "SB-124"
    damt2 = 1500
    print("New a/c No.: ", acno2, "Deposit Amount:", damt2)
    bank.create_account(acno2, damt2)

    wamt1 = 600
    print("\nDeposit Rs.", wamt1, "to A/c No.", acno1)
    bank.make_deposit(acno1, wamt1)

    wamt2 = 350
    print("Withdraw Rs.", wamt2, "From A/c No.", acno2)
    bank.make_withdrawal(acno2, wamt2)

    print("A/c. No.", acno1)
    bank.check_balance(acno1)

    print("A/c. No.", acno2)
    bank.check_balance(acno2)

    wamt3 = 1200
    print("Withdraw Rs.", wamt3, "From A/c No.", acno2)
    bank.make_withdrawal(acno2, wamt3)

    acno3 = "SB-134"
    print("A/c. No.", acno3)
    bank.check_balance(acno3)  # Non-existent account number