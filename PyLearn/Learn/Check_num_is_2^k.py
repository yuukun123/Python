# kiểm tra xem n có phải 2^k hay khong

#cách 1
def check(n):
    k = 0
    while True:
        if n == pow(2,k):
            return True
        elif n < pow(2,k):
            return False
        k += 1

n = int(input('Nhập số nguyên dương n: '))

if check(n):
    print(f'{n} là số 2^k')
else:
    print(f'{n} không phải là số 2^k')

# cách 2
# công thức n > 0 && n & (n - 1) == 0
# sử dụng tính chất bit & chất bit - 1 để ktra xem n có phải là số 2^k hay k
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

n = int(input('Nhập số nguyên dương n: '))

if is_power_of_two(n):
    print(f'{n} là số 2^k')
else:
    print(f'{n} không phải là số 2^k')
