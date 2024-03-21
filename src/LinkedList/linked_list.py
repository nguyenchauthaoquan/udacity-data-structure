from src.LinkedList.node import LinkedListNode


class LinkedList:
    """
    The singly-linked list.
    """

    def __init__(self, items=None):
        """
        Initialize the singly-linked list
        """
        if items is None:
            items = []

        self.head = None
        self.tail = None

        for item in items:
            self.append(item)

    def push(self, value):
        """
        Add the specified element at the beginning of the linked list.
        @param value: The value to be added to the linked list
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        """
        Add the specified element at the end of the linked list.
        @param value: The value to be added to the linked list
        """
        new_node = LinkedListNode(value)

        if self.head is None:
            self.push(value)
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add(self, position, value):
        """
        Add the specified element at the specified position of the linked list.
        @param position: The index at which the specified element is to be inserted
        @param value: The value to be added to the linked list
        """
        if position is None or not isinstance(position, int):
            raise IndexError()

        if position <= 0:
            self.push(value)
        else:
            new_node = LinkedListNode(value=value)
            current = self.head

            for _ in range(position - 1):
                if current is None:
                    break
                current = current.next

            if current is None:
                self.append(value=value)
            else:
                new_node.next = current.next
                current.next = new_node

    def poll(self):
        """
        Retrieves and removes the head (first element) of the linked list.
        @return: The head of this list, or null if this list is empty.
        """
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_value

    def pop(self, position=-1):
        """
        Removes the element at the specified position or the tail of the linked list.
        @param position: The position of the element from linked list, defaults to -1
        @return: the removed node value from the linked list
        """
        if position <= 0:
            return self.poll()
        else:
            current = self.head

            # if the position is out of range of the doubly linked list, remove the tail of the linked list
            for _ in range(position - 1):
                if current is None:
                    return self.pop()
                current = current.next

            if current is None or current.next is None:
                return None

            removed_value = current.next.value
            current.next = current.next.next
            return removed_value

    def remove(self, value):
        """
        Remove the element from the linked list
        @param value: the new element to be added at the specific position of the linked list
        """

        if self.head is None:
            return
        if self.head.value == value:
            self.poll()
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def index(self, value):
        """
        Get the index of the linked list based on the element of the linked list
        @param value: the value from the linked list
        @return: the index of value in linked list
        """
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1
    
    def copy(self):
        """
        Copy each item of the original linked list to the new one
        @return: the new linked list
        """
        cloned_linked_list = LinkedList()
        current = self.head

        while current is not None:
            cloned_linked_list.append(current.value)
            current = current.next

        return cloned_linked_list

    def union(self, linked_list):
        """
        Finds the union between 2 provided linked lists.
        @param linked_list: the 2nd linked list
        @return: the linked list including the union between 2 provided linked lists.
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        union_linked_list = self.copy()
        current = linked_list.head

        while current is not None:
            if current.value not in union_linked_list:
                union_linked_list.append(current.value)
            current = current.next

        return union_linked_list

    def intersection(self, linked_list):
        """
        Finds the intersection between two provided linked lists
        @param linked_list: the 2nd linked list
        @return: the linked list including the intersection between 2 provided linked lists
        """
        if (self is None or self.head is None) and (linked_list is None or linked_list.head is None):
            return []

        intersection_linked_list = LinkedList()
        current = self.head

        while current:
            if current.value in linked_list:
                intersection_linked_list.append(current.value)
            current = current.next

        return intersection_linked_list

    def display(self):
        """
        Prints the linked list to console
        """
        current = self.head
        result = []

        while current is not None:
            result.append(str(current.value))
            current = current.next

        print(" => ".join(result))

    def __contains__(self, value):
        """
        Checks if the given item is in the linked list
        @param value: the item to be checked
        @return: true if the item is in the linked list, otherwise return false
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        """
        Gets the size of the linked list
        @return: the number of items in the linked list
        """
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(7)
linked_list.display()

linked_list2 = LinkedList()

linked_list2.display()

linked_list3 = linked_list.intersection(linked_list2)
linked_list3.display()

linked_list4 = linked_list.union(linked_list2)
linked_list4.display()
