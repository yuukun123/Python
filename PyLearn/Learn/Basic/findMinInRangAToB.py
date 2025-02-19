a = [1, 3, 9, 0, 19, 29, 39, 0, 19, 49]
print(f"Nhap A va B trong khoang tu 0 den {len(a)}")
A = int(input('Nhập số A: '))
B = int(input('Nhập số B: '))

result = a[0]
for i in range(len(a)):
    if A <= a[i] <= B:
        result = min(a[i], result)

print(f"Gia tri nho nhat trong khoang tu {A} den {B} la: {result}")