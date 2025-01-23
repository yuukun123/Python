m = list(input().split())

max_caps = ""
max_caps_count = 0

for i in m:
    upper_count = sum(1 for char in i if char.isupper())  # Đếm số ký tự in hoa
    if upper_count > max_caps_count:
        max_caps = i
        max_caps_count = upper_count

print(max_caps)