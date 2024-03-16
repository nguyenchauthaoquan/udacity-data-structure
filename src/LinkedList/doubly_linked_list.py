from src.LinkedList.node import DoublyLinkedListNode


class DoublyLinkedList:
    """
    The doubly linked list
    """

    def __init__(self, items=None):
        """
        Initialize the doubly linked list with the provided list or not
        @param items: the provided list items
        """
        self.head = None
        self.tail = None

        if items is None:
            items = []

        if len(items) > 0:
            for item in items:
                self.append(item)

    def push(self, value):
        """
        Add the new element at the head of the doubly linked list
        @param value: the new element to be added at the head of the doubly linked list
        """
        new_node = DoublyLinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, value):
        """
        Add the new element at the tail of the doubly linked list
        @param value: the new element to be added at the tail of the doubly linked list
        """
        new_node = DoublyLinkedListNode(value=value)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add(self, position, value):
        """
        Add a new element at the specific position into the doubly linked list
        @param position: the position of doubly linked list
        @param value: the new element to be added at the specific position of the doubly linked list
        """
        new_node = DoublyLinkedListNode(value=value)

        if not isinstance(position, int) or position is None:
            raise IndexError()

        if position > 0:
            current = self.head
            index = 0

            while current is not None and index < position:
                current = current.next

            if current is None:
                self.append(value=value)
            else:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
        elif position <= 0:
            self.push(value=value)

    def poll(self):
        """
        Remove the head of the doubly linked list and return the removed element
        @return: the element to be removed from the doubly linked list
        """
        current = self.head

        if current is None:
            return None
        self.head = current.next

        if self.head is not None:
            self.head.prev = None

        if current is self.tail:
            self.pop()
        return current.value

    def pop(self, position=-1):
        """
        Remove the tail or the specific position of the doubly linked list and return the removed value
        @param position: The position of the element from doubly linked list, defaults to -1
        @return: the removed node value from the doubly linked list
        """
        # removes the tail of the doubly linked list if the position is negative.
        if position <= 0:
            current = self.tail

            if current is None:
                return None
            self.tail = current.prev

            if self.tail is not None:
                self.tail.next = None

            if current is self.head:
                self.poll()

            return current.value

        current = self.head

        # if the position is out of range of the doubly linked list, remove the tail of the linked list
        for _ in range(position):
            if current is None:
                return self.pop()
            current = current.next
        # remove the item from the specific position of the doubly linked list.
        if current is None:
            return None

        if current is self.head:
            self.head = current.next
        else:
            current.prev.next = current.next

        if current is self.tail:
            self.tail = current.prev
        else:
            current.next.prev = current.prev

        return current.value

    def remove(self, value):
        """
        Remove the element from the doubly linked list
        @param value: the new element to be added at the specific position of the doubly linked list
        """
        removed_node = None
        current = self.head

        while current is not None:
            if current.value == value:
                removed_node = current
                break
            current = current.next

        if removed_node is None:
            return None

        if removed_node == self.head:
            self.poll()
        elif removed_node == self.tail:
            self.pop()
        else:
            next_node = removed_node.next
            prev_node = removed_node.prev
            next_node.prev = prev_node
            prev_node.next = next_node

    def index(self, value):
        """
        Get the index of the doubly linked list based on the element of the double linked list
        @param value: the value from the doubly linked list
        @return: the index of value in doubly linked list
        """
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def __contains__(self, item):
        """
        Checks if the given item is in the doubly linked list
        @param item: the item to be checked
        @return: true if the item is in the doubly linked list, otherwise return false
        """
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def display(self):
        """
        Prints the doubly linked list to console
        """
        current = self.head
        result = []

        while current is not None:
            result.append(str(current.value))
            current = current.next

        print(" <=> ".join(result))

    def __len__(self):
        """
        Gets the size of doubly linked list
        @return: the number of items in the doubly linked list
        """
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count
