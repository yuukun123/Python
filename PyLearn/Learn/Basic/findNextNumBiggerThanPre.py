num = [1, 5, 2, 4, 3]

for i in range(1, len(num)):
    if num[i] > num[i - 1]:
        print(num[i])