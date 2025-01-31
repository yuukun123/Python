m = []
def findPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def findPrimeAndMoveToNewList(n,a):
    for x in n[:a]:
        if findPrime(x):
            m.append(x)

n = list(map(int, input("Nhập danh sách số nguyên: ").split()))
a = int(input("Nhập số nguyên a: "))
findPrimeAndMoveToNewList(n, a)
print(m)