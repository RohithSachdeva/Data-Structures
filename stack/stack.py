"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from snglnk import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size
        # other option return len(self.storage)

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1


    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()



"""
Last in, first out
Can only access the last ... 12345 .. can only access 5 
"""


"""
Queues ... Add in order 12345
Add after the 5...; Can only access 1 
Can take off 1, can take off 2 ...  
"""