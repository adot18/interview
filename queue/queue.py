
class Queue(object):

    def __init__(self):
        self.items = []

    #isEmpty
    def is_empty(self):
        return self.items == []
    #Enqueue
    def enqueue(self, val):
        self.items.insert(0, val)
    # Everything is added to position 0 and moved to the right

    #Dequeue
    def dequeue(self):
    # Removes last item from the list and returns it
        return self.items.pop()


    #size
    def size(self):
        return len(self.items)

 # return

    def __str__(self):
        return self.items
