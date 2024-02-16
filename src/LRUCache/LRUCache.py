from src.LRUCache import DoublyLinkedList


class LRUCache:
    def __init__(self, capacity: int):
        self.caches = {}
        self.linked_list = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        if key in self.linked_list:
            self.linked_list.remove(key)
            self.linked_list.append(key)

            return self.linked_list.get(key)
        return -1

    def set(self, key, value):
        if key in self.caches:
            self.linked_list.remove(self.caches[key])
        self.linked_list.append(value)
        self.caches[key] = value
        if len(self.caches) > self.capacity:
            self.linked_list.poll()


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached its capacity and 3 was the least recently used entry
