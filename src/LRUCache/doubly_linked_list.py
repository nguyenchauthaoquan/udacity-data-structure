from node import Node


class DoublyLinkedList:
    """
    Create the doubly linked list
    """

    def __init__(self):
        """
        Initialize the doubly linked list
        """
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, value):
        """Add the new node at the end of the list

        Args:
            value (any): The new value of the new node of linked list
        """
        new_node = Node(value)
        prev_tail = self.tail.prev
        prev_tail.next = new_node
        self.tail.prev = new_node
        new_node.prev = prev_tail
        new_node.next = self.tail

    def insert(self, position, value):
        """
        Add the new item to doubly linked list at the specific position

        Args:
            position (int): The position of doubly linked list
            value (any): The new value item

        Raises:
            IndexError: _description_
        """
        new_node = Node(value=value)
        current = self.head.next
        index = 0

        if position >= 0:
            while current != self.tail and index < position:
                current = current.next
                index += 1

            if index == position:
                prev_node = current.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = current
                current.prev = new_node
            else:
                self.append(value)
        else:
            raise IndexError("Invalid position")
        
    def push(self, value):
        """Add new value to the doubly linked list

        Args:
            value (any): The new value item
        """
        new_node = Node(value)
        
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

    def remove(self, value):
        """
        Remove the specific node from doubly linked list

        Args:
            node (any): the specific node node
        """
        current_node = self.head.next
        
        while current_node != self.tail:
            if current_node.value == value:
                prev_node = current_node.prev
                next_node = current_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                
            current_node = current_node.next
    
    def pop(self):
        if self.head.next != self.tail:
            current_node = self.head.next
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            
            return current_node
        return None
    
    def get(self, value):
        """
        Get the node based on the value

        Args:
            value (any): the specific value
        """
        current_node = self.head.next
        
        while current_node != self.tail:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        
        return None

    def display(self):
        """
        Print the items of doubly linked list
        """
        current = self.head
        results = []

        if self.head is not None:
            while current is not None:
                results.append(str(current.value))
                current = current.next

        print(" <=> ".join(results))

