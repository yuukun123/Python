class shoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item_name, item_price):
        item = (item_name, item_price)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

    def display(self):
        print("Shopping Cart:")
        for item in self.items:
            print(f"{item[0]} - ${item[1]:.2f}")

