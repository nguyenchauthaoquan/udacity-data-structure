class Node:
    """
    A node as item in linked list
    """

    def __init__(self, value=None):
        """
        Initialize the object from Node class
        @param value: The node value
        """
        self.value = value
        self.next = None
        self.prev = None
