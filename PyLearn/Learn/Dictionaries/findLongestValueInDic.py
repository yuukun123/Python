def findLongestValueInDic(n):
    if not n:
        return None
    longest_key = max(n, key=len)
    return n[longest_key]

n = {}
pairs = input().split() # Nhập danh sách các cặp key-value cách nhau bởi dấu cách

if len(pairs) % 2 != 0:  # Kiểm tra lỗi nhập lẻ số phần tử
    print("Dữ liệu nhập không hợp lệ.")
else:
    for i in range(0, len(pairs), 2):  # Duyệt từng cặp (key, value)
        key = pairs[i] # Lấy key từ danh sách
        value = pairs[i + 1] # Chuyển đổi value từ chuỗi sang số nguyên
        n[key] = value  # Thêm cặp key-value vào dictionary

print(findLongestValueInDic(n))