m = list(map(int, input().split()))
found = False
max_negative = float('-inf')

for i in m:
    if i < 0:
        max_negative = max(max_negative, i)
        found = True
if found:
    print(max_negative)
else:
    print(0)

# cách tối ưu
m = list(map(int, input("Nhập danh sách số nguyên: ").split()))

# Lọc ra các số âm trong danh sách
negative_numbers = [x for x in m if x < 0]

# Kiểm tra và tìm số âm lớn nhất
if negative_numbers:
    print(max(negative_numbers))
else:
    print(0)
