import sys
import unittest

from src.Tree.huffman_coding import HuffmanTree


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        Initialize the testing class
        """
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.sequence = "The bird is the word"
        self.huffman = HuffmanTree()

    def test_edge_case_1(self):
        encoded_sequence, _ = self.huffman.huffman_encoding(self.sequence)
        self.assertLess(sys.getsizeof(self.sequence), sys.getsizeof(sys.getsizeof(int(encoded_sequence, base=2))))  # add assertion here


if __name__ == '__main__':
    unittest.main()
