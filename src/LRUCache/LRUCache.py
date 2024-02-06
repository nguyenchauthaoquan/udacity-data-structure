from LinkedList.doubly_linked_list import DoublyLinkedList


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
        self.caches = {}
        self.linked_list = DoublyLinkedList()

    def get(self, key):
        if key in self.caches:
            value = self.caches[key]
            self.linked_list.pop()
            self.linked_list.append(value)
            return value[1]
        return -1

    def set(self, key, value):
        if key in self.caches:
            self.linked_list.remove(self.caches[key])
        
        self.linked_list.append((key, value))
        self.caches[key] = (key, value)
        
        if len(self.caches) > self.capacity:
            self.linked_list.pop()
            del self.caches[key]
            


lru = LRUCache(capacity=5)
lru.set(1,1)
lru.set(2,2)
lru.set(3,3)
lru.set(4,4)

print("After setting 11, 22, 33, 44")
lru.linked_list.display()

print(lru.get(1))

print(lru.get(2))

print(lru.get(9))

lru.set(5, 5) 
print("After setting 55")

lru.linked_list.display()
lru.set(6, 6)
print("After setting 66")

lru.linked_list.display()

print(lru.get(3))

print(lru.caches)