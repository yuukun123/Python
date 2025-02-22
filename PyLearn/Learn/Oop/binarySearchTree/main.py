from BinarySearchTree import BinarySearchTree

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(6)
    bst.insert(1)
    bst.insert(2)
    bst.insert(7)
    bst.insert(8)
    bst.insert(9)

    print("Tree: ", end = "")
    bst.print_LRN()
    print()

    bst.delete(3)
    print("Tree after delete 3: ", end = "")
    bst.print_LRN()
    print()

    if bst.search(4) is not False:
        print("Found 4")
    else:
        print("Not found 4")

    if bst.search(10) is not False:
        print("Found 10")
    else:
        print("Not found 10")