m = list(map(int, input().split()))
count = 0
max_so_far = float('-inf')

for i in m:
    if i > max_so_far:
        max_so_far = i
        count += 1

print(count)