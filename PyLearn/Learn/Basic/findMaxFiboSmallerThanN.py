def fibo(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def findMaxFiboSmallerThanN(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    fibo(n)
    print("The maximum Fibonacci number smaller than", n, "is", findMaxFiboSmallerThanN(n))
