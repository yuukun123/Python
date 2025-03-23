from shop import shop

class menu:
    def menuSystem(self):
        Shop = shop()
        while True:
            print("\n=== Quản lý cửa hàng ===")
            print("1. add product")
            print("2. remove product")
            print("3. show list product")
            print("4. search product")
            print("5. exit")
            choice = input("Chọn chức năng (1-5): ")

            if choice == "1":
                Shop.addListProduct()
            elif choice == "2":
                Shop.removeProduct()
            elif choice == "3":
                Shop.showListProduct()
            elif choice == "4":
                Shop.searchProduct()
            elif choice == "5":
                exit()
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")