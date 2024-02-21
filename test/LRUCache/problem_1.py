import string
import unittest
import random
from random import randrange

from src.LRUCache.LRUCache import LRUCache


class LRUCacheTest(unittest.TestCase):
    def test_edge_case_1(self):
        cache = LRUCache(capacity=5)

        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        self.assertEqual(cache.get(1), 1)  # returns 1
        self.assertEqual(cache.get(2), 2)  # returns 2
        self.assertEqual(cache.get(9), -1)  # returns -1

        cache.set(5, 5)
        cache.set(6, 6)

        self.assertEqual(cache.get(3), -1)  # returns -1

    def test_edge_case_2(self):
        cache = LRUCache(capacity=5)

        cache.set(1, 2)
        cache.set(2, 3)
        cache.set(3, 4)
        cache.set(4, 5)

        self.assertEqual(cache.get(3), 4)  # returns 4
        self.assertEqual(cache.get(4), 5)  # returns 5
        self.assertEqual(cache.get(9), -1)  # returns -1

    def test_edge_case_3(self):
        cache = LRUCache(capacity=1)
        cache.set(0, 0)
        cache.set(1, 1)
        self.assertEqual(cache.get(0), -1)
        self.assertEqual(cache.get(1), 1)
        cache.set(2, 2)
        self.assertEqual(cache.get(2), 2)

        self.assertEqual(cache.get(3), -1)

    def test_edge_case_4(self):
        cache = LRUCache(capacity=3)

        cache.set(1, 1)
        cache.set(2, 2)

        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

        cache.set(3, 3)

        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), -1)

    def test_exception_case_1(self):
        with self.assertRaises(ValueError):
            LRUCache(capacity=-1)

    def test_exception_case_2(self):
        with self.assertRaises(TypeError):
            LRUCache(capacity=''.join(random.choices(string.ascii_lowercase +
                                                     string.digits, k=randrange(10))))

    def test_exception_case_3(self):
        with self.assertRaises(TypeError):
            LRUCache(capacity=None)


if __name__ == '__main__':
    unittest.main()
