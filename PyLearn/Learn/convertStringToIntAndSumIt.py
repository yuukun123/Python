n = "3, 12, 15"

def convertStringToIntAndSumIt(n):
    n = n.split(", ")
    sum = 0
    for i in n:
        sum += int(i)
    return sum

print(convertStringToIntAndSumIt(n))