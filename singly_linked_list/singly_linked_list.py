class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)  # Created a node and passed in the value
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        # Tail is new_node which has a default passed in value of self.next = None; so mimics the end of the tail
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def remove_head(self):
        if self.head is None:
            return
        self.head = self.head.next  # New

    def remove_tail(self):
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        pointer = self.head
        while pointer.next is not self.tail:  # While it is not the tail, we will continue going
            pointer = pointer.next
        self.tail = pointer
        self.tail.next = None


# Dealing with nodes that have a pointer
"""
Node with a pointer thats called next


"""
