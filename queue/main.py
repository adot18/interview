from queue import Queue
def main():
    q = Queue()
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    print(q.__str__())
    q.dequeue()
    q.dequeue()
    print(q.__str__())

if __name__ == "__main__":
    main()

