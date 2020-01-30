import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.max = 0
        self.order = DoublyLinkedList()
        self.storage = dict()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else: 
            return None 

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
    # create a node if key not found and move to front 
    # Move node to front if key found
    # if full remove last node from linked list AND dictionary

        if key in self.storage: # check to see if key is in storage 
            node = self.storage[key] # get key a store it in storage 
            node.value = (key, value) # assign the value to a touple of key and value 
            self.order.move_to_end(node) # removeing a tail node in the list beacuse we added and need to make space
            return
        if self.max == self.limit: # if the max is equal to the limit in the list
            del self.storage[self.order.head.value[0]] # we want to delete the head value to make room
            self.order.remove_from_head() # removing head 
            self.max -= 1 # initializing deletion
        self.order.add_to_tail((key, value)) # adding our key value tuple to the tail
        self.storage[key] = self.order.tail # connecting our cache to the tail of our list
        self.max += 1 #initializing added node
