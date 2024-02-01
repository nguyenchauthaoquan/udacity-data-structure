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
            
        
    
    def display(self):
        current = self.head
        results = []
        
        if self.head is not None:
            while current is not None:
                results.append(str(current.value))
                current = current.next
        
        print(" <=> ".join(results))
        

doublyLinkedList = DoublyLinkedList()

doublyLinkedList.append(1)
doublyLinkedList.append(2)
doublyLinkedList.append(3)
doublyLinkedList.append(4)

doublyLinkedList.display()

doublyLinkedList.insert(position=0, value=5)
doublyLinkedList.display()

doublyLinkedList.insert(2, 1.5)
doublyLinkedList.display()

doublyLinkedList.insert(3, 2.5)
doublyLinkedList.display()

doublyLinkedList.insert(11, 4.5)
doublyLinkedList.display()