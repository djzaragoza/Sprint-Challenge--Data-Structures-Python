class Node:  # node class given 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList: # Linked List class given 
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev): 
    #   # Objective:
    #   # initialize pointers, previous and node as None
    #   # iterate thru linked list
    #   ## need to setup the next node coming up as current next node via what used to be old node
    #   ## previous node becomes the current_node and current_node becomes next node
    #   ## head moves to previous node 
    
    #   ## ran test and returned successful with runtime of .011s!
    
        prev = None
        node = None
        current_node = self.head
        
        while current_node is not None:
            next = current_node.next_node
            current_node.next_node = prev
            prev = current_node
            current_node = next
            self.head = prev
        return prev 
        pass 
