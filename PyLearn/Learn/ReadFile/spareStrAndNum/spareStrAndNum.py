# def spareStrAndNum():
#     try:
#         with open("chuoi.inp", "r") as fr, open("chuoi.out", "w") as fw:
#             for s in map(str.strip,fr):
#                 num = []
#                 strings = []
#                 for i in range(len(s)):
#                     if s[i].isdigit():
#                         num.append(s[i])
#                     else:
#                         strings.append(s[i])
#                 if num == []:
#                     num.append("-")
#                 fw.write("".join(strings) + "\n")
#                 fw.write("".join(num) + "\n")
#
#     except FileNotFoundError:
#         print("File not found")

# tối ưu hơn
def spareStrAndNum():
    try:
        with open("chuoi.inp", "r") as fr, open("chuoi.out", "w") as fw:
            s = fr.read().strip()

            num = "".join(filter(str.isdigit, s)) or "-"
            strings = "".join(filter(str.isalpha, s)) or "-"

            fw.write(strings + "\n")
            fw.write(num + "\n")

    except FileNotFoundError:
        print("File not found")

spareStrAndNum()