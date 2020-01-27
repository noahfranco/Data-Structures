import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # adding to the tail of the linked list 
        self.storage.add_to_tail(value)
        self.size += 1


    def dequeue(self, value):
        # make sure to check size before remove
        if self.size < 0:
            return None 
        self.storage.remove_from_head(value)
        self.size -= 1
        
        

    def len(self):
        return self.size
