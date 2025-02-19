# n = 123456789
# m = list(map(int, str(n)))

m = list(map(int, input().split()))

if all(x == m[0] for x in m):
    print("True")
else:
    print("False")