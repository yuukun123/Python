def findKeyWithMaxValue(n):
    if not n:
        return None
    return max(n, key=n.get)

n = {}
pairs = input().split() # Nhập danh sách các cặp key-value cách nhau bởi dấu cách

for i in range(0, len(pairs), 2):  # Duyệt từng cặp (key, value)
    key = pairs[i] # Lấy key từ danh sách
    value = int(pairs[i + 1]) # Chuyển đổi value từ chuỗi sang số nguyên
    n[key] = value  # Thêm cặp key-value vào dictionary

print(findKeyWithMaxValue(n))

