from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    LRU cache implementation
    """

    def __init__(self, capacity):
        """
        Inititalize the LRU cache

        Args:
            capacity (int): The cache capacity
        """
        self.capacity = capacity
        self.cache = {}
        self.linked_list = DoublyLinkedList()

    def get(self, key):
        pass

    def set(self, key, value):
        pass


lru = LRUCache(capacity=5)
lru.set(1,1)
lru.set(2,2)
lru.set(3,3)
lru.set(4,4)
lru.linked_list.display()

print(lru.get(1))
print(lru.get(2))
print(lru.get(9))

lru.set(5, 5) 
lru.set(6, 6)
lru.linked_list.display()

print(lru.get(3))

