import math

a = int(input())
b = int(input())

def UC(n):
    new = []
    for i in range(1, n + 1):
        if (n % i == 0):
            new.append(i)
    return new

combie = set(UC(a)).intersection(set(UC(b)))

print(sorted(combie))

