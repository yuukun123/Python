from Node import Node

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        if node is not None:
            if self.isEmpty():
                self.top = node
            else:
                node.next = self.top
                self.top = node

    def peek(self):
        return self.top

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def __str__(self):
        values = []
        node = self.top
        while node is not None:
            values.append(str(node.value))
            node = node.next
        return " -> ".join(values)


