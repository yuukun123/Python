from product import product

class shop(product):
    def __init__(self):
        self.listProduct = []

    def addProduct(self):
        print()
        name = input("Nhập tên sản phẩm: ")
        description = input("Nhập mô tả sản phẩm: ")
        while True:
            try:
                price = float(input("Nhập giá sản phẩm (0 < giá <= 100): "))
                if 0 < price <= 100:
                    break
                else:
                    print("Giá phải nằm trong khoảng 0 đến 100! Vui lòng nhập lại.")
            except ValueError:
                print("Giá phải là số! Vui lòng nhập lại.")

        # Tạo sản phẩm mới
        new_product = product(name, description, price)

        # Nhập đánh giá (có thể nhập nhiều lần)
        while True:
            rate_input = input("Nhập đánh giá (1-5), nhập 'q' để dừng: ")
            if rate_input.lower() == 'q':
                break
            try:
                rate = int(rate_input)
                new_product.addRate(rate)
            except ValueError:
                print("Đánh giá phải là số nguyên! Vui lòng nhập lại.")
        print()
        # Thêm sản phẩm vào danh sách
        self.listProduct.append(new_product)
        print(f"Đã thêm sản phẩm '{name}' thành công!")

    def addListProduct(self):
        n = int(input("Quantity product: "))
        for _ in range(n):
            self.addProduct()

    def removeProduct(self):
        if not self.listProduct:
            print("list is empty")
            return

        nameRemove = input("nhập tên sản phẩm muốn xóa: ")
        found = False
        for i, product in enumerate(self.listProduct):
            if nameRemove == product.getName():
                removed_product = self.listProduct.pop(i)
                print(f"{removed_product.getName()} is remove ")
                found = True
                break
        if not found:
            print("không có sản phẩm muốn xóa trong list")

    def searchProduct(self):
        nameSearch = input("Name product to search: ")
        found = False
        for i, product in enumerate(self.listProduct):
            if nameSearch == product.getName():
                print(product.viewInfo())
                found = True
                break
        if not found:
            print("không có sản phẩm muốn xóa trong list")


    def showListProduct(self):
        if not self.listProduct:
            print("list is empty")
        else:
            for i, product in enumerate(self.listProduct, 1):
                print(f"\nSản phẩm {i}:")
                print(product.viewInfo())
                print("-" * 60)