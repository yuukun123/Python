n = "Hello Word 1 3 4"

coutDigit = 0
countUpper = 0
countLower = 0

for i in n:
    if i != ' ':
        if i.isdigit():
            coutDigit += 1
        elif i.isupper():
            countUpper += 1
        else:
            countLower += 1

print(coutDigit)
print(countUpper)
print(countLower)