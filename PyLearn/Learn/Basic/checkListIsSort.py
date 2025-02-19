m = list(map(int, input().split()))
isSort = False

for i in range(1, len(m)):
    if m[i] < m[i - 1]:
        isSort = False
        break
    else:
        isSort = True

print(isSort)

# cách tối ưu
m = list(map(int, input("Nhập danh sách số nguyên: ").split()))

print(all(m[i] <= m[i + 1] for i in range(len(m) - 1)))

# cách 2
m = list(map(int, input("Nhập danh sách số nguyên: ").split()))

if m == sorted(m):
    print("True")
else:
    print("False")