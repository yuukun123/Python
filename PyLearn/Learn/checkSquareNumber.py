def checkSquareNumber(n):
    if int(n ** 0.5) ** 2 == n:
        return True
    else:
        return False

print(checkSquareNumber(100))