from src.LRUCache import DoublyLinkedList


class LRUCache:
    def __init__(self, capacity):
        self.caches = {}
        self.linked_list = DoublyLinkedList()
        if isinstance(capacity, int):
            if capacity >= 0:
                self.capacity = capacity
            else:
                raise ValueError()
        else:
            raise TypeError()

    def get(self, key):
        """
        Gets the cached key from the caches
        @param key: The key to get from caches
        """
        if key in self.linked_list:
            self.linked_list.remove(self.caches[key])
            self.linked_list.append(self.caches[key])

            return self.caches[key]
        return -1

    def set(self, key, value):
        """
        Sets the key value pair to the current caches
        @param key: The cache key
        @param value: The cache value
        """
        if key in self.caches:
            self.linked_list.remove(self.caches[key])
            self.linked_list.append(value)
        else:
            if len(self.caches) >= self.capacity:
                del self.caches[self.linked_list.poll()]
            self.caches[key] = value
            self.linked_list.append(value)
