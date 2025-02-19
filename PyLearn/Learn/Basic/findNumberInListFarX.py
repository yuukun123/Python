m = [1, 5, 9, 100 ,3 ,12 ,40 ,50 ,8]
x = 9
max_distance = -1
farthest_value = None

for i in range(len(m)):
    distance = abs(m[i] - x)
    if distance > max_distance:
        max_distance = distance
        farthest_value = m[i]

print(farthest_value)

# cash tối ưu
L = list(map(int, input("Nhập danh sách số nguyên: ").split()))
x = int(input("Nhập số nguyên x: "))

# Tìm giá trị xa x nhất bằng max() với key
farthest_value = max(L, key=lambda num: abs(num - x))

print("Giá trị xa x nhất là:", farthest_value)
