n = 375469485
a = str(n)
result = ''
for i in range(len(a)):
    if i > 0 and (len(a) - i) % 3 == 0 and a[i] != '0':
        result += '.'
    result += a[i]

print(result)