from src.LRUCache.LRUCache import LRUCache

if __name__ == '__main__':
    print('***** Testcase 1 *****')
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

    # Testcase 2
    print('***** Testcase 2 *****')
    our_cache2 = LRUCache(1)
    our_cache2.set(0, 0)
    our_cache2.set(1, 1)
    print(our_cache2.get(0))
    print(our_cache2.get(1))
    our_cache2.set(2, 2)
    print(our_cache2.get(2))
    print(our_cache2.get(3))

    # Testcase 3
    print('***** Testcase 3 *****')
    our_cache2 = LRUCache(3)
    our_cache2.set(1, 1)
    our_cache2.set(2, 2)
    print(our_cache2.get(1))
    print(our_cache2.get(2))
    our_cache2.set(5, 5)
    print(our_cache2.get(5))
    print(our_cache2.get(6))