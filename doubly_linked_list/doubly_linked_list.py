"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        # Default length of 1 if there exists a node in the list.
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return
        temp = self.head.value  # Temporary store of head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            self.head.next.prev = None  # Changing the backwards pointer to point to nothing
            self.head = self.head.next
            self.length -= 1
            return temp

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 0:
            return

        temp = self.tail.value
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return temp

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.length == 0:
            return
        elif self.head is node:
            return
        elif self.tail is not node:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.head.prev = None

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length == 0:
            return
        if self.tail is node:
            return
        if self.head is not node:
            node.prev.next = node.next
        else:
            self.head = node.next
        node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length == 0:
            return None

        temp = node.value

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        if self.head is node:
            self.head = node.next
        elif self.tail is node:
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.length -= 1
        return temp

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass
