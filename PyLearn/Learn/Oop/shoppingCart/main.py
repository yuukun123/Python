from shoppingCart import shoppingCart

if __name__ == '__main__':
    cart = shoppingCart()
    cart.add('apple', 2)
    cart.add('banana', 3)
    cart.add('orange', 4)

    cart.display()
    print("Total: $" + str(cart.calculate_total()))

    print("\nafter remove apple")
    cart.remove_item('banana')
    cart.display()
    print("Total: $" + str(cart.calculate_total()))