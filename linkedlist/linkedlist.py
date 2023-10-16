from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def set_head(self, head_node):
        self.head = head_node

    def get_head(self):
        return self.head

    # Working
    def pop(self):
        head = self.head
        if head:
            temp = head
            self.head = head.next
            return temp
        else:
            raise IndexError("Cannot pop from an empty list")
    # Working
    def push(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.set_head(node)

    # Not Working
    def append(self, value):
        node = Node(value)
        head = self.head
        if head is None:
            self.head = node
            return

        while head.next:
            head.next.next = node
            head.next.next.next = None

        if head.next is None:
            head.next = node
            head.next.next = None
    # Working
    def contains(self, value):
        node = Node(value)

        head = self.head
        if head is None:
            return False
        while head:
            if head.data == node.data:
                return True
            head = head.next

    def delete_instances(self, value):
        node = Node(value)

        head = self.head
        if head is None:
            return False

        if head.data == node.data:
            temp_node = head.next
            head = temp_node
            head.next = temp_node.next

        while head.next:
            temp = head.next
            if temp.data == node.data:
                head.next = temp.next
            head = head.next

    def length(self):
        if self.head is None:
            return 0
        temp_head = self.head
        count = 0
        while temp_head:
            count += 1
            temp_head = temp_head.get_next()
        return count

    def __str__(self):
        head = self.head
        output = ''
        while head:
            output += str(head.get_data()) + '->'
            head = head.next

        return output
