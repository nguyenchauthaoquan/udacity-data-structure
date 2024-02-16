from src.LRUCache import DoublyLinkedList, Node


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


our_cache1 = LRUCache(5)
our_cache1.set(1, 1)
our_cache1.set(2, 2)
our_cache1.set(3, 3)
our_cache1.set(4, 4)
print(our_cache1.get(1))  # returns 1
print(our_cache1.get(2))  # returns 2
print(our_cache1.get(9))  # returns -1 because 9 is not present in the cache
our_cache1.set(5, 5)
our_cache1.set(6, 6)
# returns -1 because the cache reached it's capacity and 3 was the LRU entry
print(our_cache1.get(3))
