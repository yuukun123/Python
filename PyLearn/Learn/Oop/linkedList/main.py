from linkedList import linkedList

if __name__ == "__main__":
    l = linkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)

    print("Linked List:")
    l.display()

    l.delete(2)
    print("Linked List after deleting 2:")
    l.display()