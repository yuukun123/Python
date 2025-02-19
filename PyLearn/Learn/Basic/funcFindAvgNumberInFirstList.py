def findAvgNumberInFirstList(n, a):
    if a > len(n) or a <= 0 or not n:
        return -1
    return sum(n[:a]) / a

n = list(map(int, input("Nhập danh sách số nguyên: ").split()))
a = int(input("Nhập số nguyên a: "))
result = findAvgNumberInFirstList(n, a)
print(result if result != -1 else "Không tìm thấy")
