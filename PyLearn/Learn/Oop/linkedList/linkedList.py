from Node import Node

class linkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        if current:
            while current:
                print(current.value, end="")
                if current.next:
                    print(" -> ", end="")
                current = current.next
            print()
        else:
            print("Linked List is empty")

    def insert(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next

        if current:
            prev.next = current.next