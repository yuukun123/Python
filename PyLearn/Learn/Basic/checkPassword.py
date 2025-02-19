n = "1234Yuu@"
m = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-' ]

has_upper = False
has_special = False

for i in n:
    if i.isalpha() and i.isupper():
        has_upper = True
    if i in m:
        has_special = True

if  len(n) >= 8 and has_upper and has_special:
    print("strong password")
else:
    print("week password")