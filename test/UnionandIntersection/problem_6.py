import unittest

from parameterized import parameterized

from src.LinkedList.linked_list import LinkedList


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        Initialize the testing class
        """
        super(MyTestCase, self).__init__(*args, **kwargs)

    @parameterized.expand([
        [LinkedList([1, 2, 3, 4, 5, 6]), LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])],
        [LinkedList(), LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])],
        [LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), LinkedList()],
    ])
    def test_union_edge_cases(self, linked_list_1, linked_list_2):
        union_linked_list = linked_list_1.union(linked_list_2)

        self.assertGreater(len(union_linked_list), 0)
        self.assertIn(1, union_linked_list)
        self.assertIn(2, union_linked_list)
        self.assertIn(3, union_linked_list)
        self.assertIn(4, union_linked_list)
        self.assertIn(5, union_linked_list)
        self.assertIn(6, union_linked_list)
        self.assertIn(7, union_linked_list)
        self.assertIn(8, union_linked_list)
        self.assertIn(9, union_linked_list)
        self.assertIn(10, union_linked_list)

    @parameterized.expand([
        [LinkedList(), LinkedList()]
    ])
    def test_union_empty_case_2(self, linked_list_1, linked_list_2):
        union_linked_list = linked_list_1.union(linked_list_2)
        self.assertEqual(len(union_linked_list), 0)

    @parameterized.expand([
        [LinkedList([1, 2, 3, 4, 5, 6]), LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])],
    ])
    def test_intersection_edge_cases(self, linked_list_1, linked_list_2):
        intersection_linked_list = linked_list_1.intersection(linked_list_2)

        self.assertIn(1, intersection_linked_list)
        self.assertIn(2, intersection_linked_list)
        self.assertIn(3, intersection_linked_list)
        self.assertIn(4, intersection_linked_list)
        self.assertIn(5, intersection_linked_list)
        self.assertIn(6, intersection_linked_list)

    @parameterized.expand([
        [LinkedList(), LinkedList()],
        [LinkedList(), LinkedList([1, 2, 3, 4, 5, 6])],
        [LinkedList([1, 2, 3, 4, 5, 6]), LinkedList()]
    ])
    def test_intersection_empty_case(self, linked_list_1, linked_list_2):
        intersection_linked_list = linked_list_1.intersection(linked_list_2)

        self.assertEqual(len(intersection_linked_list), 0)


if __name__ == '__main__':
    unittest.main()
