def Armstrong(a):
    sum = 0
    temp = a
    d = len(str(a))
    while temp > 0:
        digit = temp % 10
        sum += digit ** d
        temp //= 10
    if a == sum:
        return True
    else:
        return False

a = int(input())
print(Armstrong(a))