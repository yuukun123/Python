from stack import Stack

if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    print(stack)
    print("after pop: ", stack.pop())
    print(stack)
    print("value of top: ", stack.peek())
