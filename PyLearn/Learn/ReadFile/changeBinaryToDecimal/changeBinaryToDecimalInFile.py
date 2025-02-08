def binToDec():
    try:
        with open("2to10.inp", "r") as fr, open("2to10.out", "w") as fw:
            # Tự động loại bỏ khoảng trắng khi đọc file, không cần gọi strip() nhiều lần
            for bin in map(str.strip,fr):
                if bin:
                    try:
                        fw.write(str(int(bin, 2)) + "\n")
                    except ValueError:
                        fw.write("Error\n")
        fr.close()
        fw.close()
    except FileNotFoundError:
        print("File not found")

binToDec()

