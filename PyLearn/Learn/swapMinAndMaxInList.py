# m = list(map(int, input().split()))
#
# max_val = max(m)
# min_val = min(m)
#
# m[m.index(max_val)] = min_val
# m[m.index(min_val)] = max_val
#
# print(m)

m = list(map(int, input().split()))

max_val = 0
min_val = 0

for i in range(len(m)):
    if m[i] > m[max_val]:
        max_val = i
    if m[i] < m[min_val]:
        min_val = i

m[max_val], m[min_val] = m[min_val], m[max_val]

print(m)