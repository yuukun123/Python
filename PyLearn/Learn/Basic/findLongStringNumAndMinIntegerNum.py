m = list(input().split())

max_length = ""
min_val = float('inf')

for i in m:
    if i.isdigit():
        min_val = min(min_val, int(i))
    else:
        if len(i) > len(max_length):
            max_length = i

if min_val == float('inf'):
    min_val = None

print(max_length, min_val)

