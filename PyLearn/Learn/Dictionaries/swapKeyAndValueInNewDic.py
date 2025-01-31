def swapKeyAndValueInNewDic(n):
    if not n:
        return None
    m = {}  # Dictionary mới
    for key, value in n.items():
        if value in m:  # Nếu đã tồn tại value làm key trong dictionary mới
            return None # Trả về None vì có key trùng nhau sau khi hoán đổi
        m[value] = key  # Thêm cặp value-key vào dictionary m
    return m  # Trả về dictionary mới nếu không có trùng key


# Test case 1: Không có giá trị trùng nhau
n1 = {"a": 1, "b": 2, "c": 3}
print(swapKeyAndValueInNewDic(n1))
# Kết quả mong đợi: {1: "a", 2: "b", 3: "c"}

# Test case 2: Có giá trị trùng nhau
n2 = {"a": 1, "b": 2, "c": 1}
print(swapKeyAndValueInNewDic(n2))
# Kết quả mong đợi: None

# Test case 3: Dictionary rỗng
n3 = {}
print(swapKeyAndValueInNewDic(n3))
# Kết quả mong đợi: None