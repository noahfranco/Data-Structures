import sys
sys.path.append('queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new value is less then old value 
            # if left side is none 
                # initialize left side to a binary tree
            # else: 
                # insert new value on left side recursively                
                # return 
        # if new value is greater then old value
            #if left side is none  
                # initialize right side to a brinary tree
            #else:
                # insert new value on right side
                # return

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value) # being recursive
        
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value) # being recursive

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # *** First thing to do is to check if the right and left side of the tree have anything ***
        # if value in self.left side of tree 
            # initialize left side to a binary tree 
            # return True 
        #else:
            #return False
        # if value in self.right side of tree 
            # initialize left side to a binary tree
            # return True 
        # else:
            # return False

        # recursive solution
        if self.value == target:
            return True 
        if target < self.value:
            if not self.left:
                return False
            else: 
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # recursive code below 
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
         # recursive code above

        # Iterative approach below
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        
        # return max_value
        # Iterative approach above 

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # value = self.node
        # if self.left < self.right
            # if self.left:
                # self.left.in_order_print(value)
            #else:
                # return None
            # if self.right:
                # self.left.in_order_print(value)
            #else:
                # return None
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #if self.left < self.right:
            # if node in self.left:
                # self.left.bft_print(node)
            # else: 
                # return None
            #if node in self.right:
                # self.right.bft_print(node)
            # else: 
                # return None 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
