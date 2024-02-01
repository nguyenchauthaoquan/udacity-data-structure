class Node:
    """
    Describe the information of linked list node.
    """

    def __init__(self, value=None):
        """
        Initialize the object from Node class
        Args:
            key (any, optional): The key of linked list node. Defaults to None.
            value (any, optional): The value of linked list node. Defaults to None.
        """
        self.value = value
        self.prev = None  # The previous node item in linked list
        self.next = None  # The next node item in linked list
