import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0

        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # adding to the tail of the linked list 
        self.storage.add_to_tail(value)
        self.size += 1


    def dequeue(self):
        # make sure to check size before remove
        if self.storage.length < 1:
            return None
        else:
            return self.storage.remove_from_head()
        

    def len(self):
        return self.storage.length
