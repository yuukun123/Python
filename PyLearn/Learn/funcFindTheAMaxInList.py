def findTheAMaxInList(n, a):
    if a > len(n):
        print("Không tìm thấy")
    n.sort(reverse=True)
    print(n)
    print(n[a-1])

n = list(map(int, input("Nhập danh sách số nguyên: ").split()))
a = int(input("Nhập số nguyên a: "))
findTheAMaxInList(n, a)
# print()
