from queue import queue

if __name__ == '__main__':
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    q.print_queue()
    print("dequeue: ", q.dequeue())