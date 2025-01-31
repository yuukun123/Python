def findElementKInList(n, k):
    for i in range(1, len(n) - 1):
        if n[i] == k:
            return i

    return -1

n = list(map(int, input("Nhập danh sách số nguyên: ").split()))
k = int(input("Nhập số nguyên k: "))
print(findElementKInList(n, k))