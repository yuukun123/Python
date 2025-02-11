def findUCLN(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def findBCNN(a, b):
    c = a, d = b
    if a == b:
        a // findUCLN(a, b)
    else:
        a = a // findUCLN(a, b)
        b = b // findUCLN(a, b)
        return a * b




a = 6
b = 10

print(findUCLN(a, b))
print(findBCNN(a, b))