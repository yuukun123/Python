def findUCLN(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def findBCNN(a, b):
    return a * b // findUCLN(a, b)

a = 6
b = 10

print(findUCLN(a, b))
print(findBCNN(a, b))
