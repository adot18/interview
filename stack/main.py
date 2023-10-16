from collections import deque
from stack import Stack

def main():
    ''' imported version
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)

    # stack.pop() will pop from the end
    stack.popleft()
    print(stack.__str__())
    '''

    s2 = Stack()

    s2.enqueue(2)
    s2.enqueue(4)
    s2.enqueue(3)
    s2.enqueue(1)
    print(s2.__str__())

    s2.pop()

    print(s2.__str__())

if __name__ == "__main__":
    main()