m = list(map(int, input().split()))
is_wave = False

for i in range(1, len(m) - 1):
    if m[i] > m[i - 1] and m[i] > m[i + 1] or m[i] < m[i - 1] and m[i] < m[i + 1]:
        is_wave = True
        break

print(is_wave)

