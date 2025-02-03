# Định nghĩa giá của từng món ăn
gia_mon_an = {
    "Gà nán": 30000,
    "Hamburger": 25000,
    "Cocacola": 10000
}

# Yêu cầu người dùng nhập số lượng từng món ăn
print("| Chào mừng các bạn đến với nhà hàng thức ăn nhanh |")
print("| Mời bạn nhập số lượng từng món ăn:    |")

so_luong = {}
for mon in gia_mon_an:
    so_luong[mon] = int(input(f"{mon}: "))

# Tính toán hóa đơn
hoa_don = {}
tong_truoc_thue = 0

for mon, gia in gia_mon_an.items():
    thanh_tien = gia * so_luong[mon]
    hoa_don[mon] = thanh_tien
    tong_truoc_thue += thanh_tien

thue = tong_truoc_thue * 0.05
tong_sau_thue = tong_truoc_thue + thue

# In hóa đơn
print("\nHóa đơn:")
print("-" * 40)
for mon, gia in gia_mon_an.items():
    print(f"{mon.ljust(15)} {str(gia) + 'đ'.ljust(10)} × {so_luong[mon]}")

print("-" * 40)
print("Tổng:")
for mon, thanh_tien in hoa_don.items():
    print(f"{mon.ljust(20)} {str(thanh_tien) + 'đ'.ljust(10)}")

print("-" * 40)
print(f"Tổng trước thuế".ljust(20), f"{str(tong_truoc_thue) + 'đ'.ljust(10)}")
print(f"Thuế(5%)".ljust(20), f"{str(int(thue)) + 'đ'.ljust(10)}")
print(f"Tổng sau thuế".ljust(20), f"{str(int(tong_sau_thue)) + 'đ'.ljust(10)}")
print("-" * 40)