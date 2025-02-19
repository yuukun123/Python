m = list(map(int, input().split()))
odd_even_list = True

for i in range(1, len(m) - 1):
    for j in range(i + 1, len(m)):
        if (m[i] + m[j]) % 2 == 0:
            odd_even_list = False

    if not odd_even_list:
        break

print(odd_even_list)
