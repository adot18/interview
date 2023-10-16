class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop(-1)

    def __sizeof__(self):
        return len(self.items)

    def __str__(self):
        return self.items
