import sys
import unittest
import string
import random
from parameterized import parameterized

from src.Tree.huffman_coding import HuffmanTree


class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        Initialize the testing class
        """
        super(MyTestCase, self).__init__(*args, **kwargs)

        self.huffman = HuffmanTree()



    @parameterized.expand([
        ["The bird is the word", ],
        ["The dog is the best friends"],
        ["AAAAAAABBBCCCCCCCDDEEEEEE"],
        ["".join(random.choices(string.ascii_letters + string.digits, k=random.randrange(100000)))]
    ])
    def test_edge_cases(self, sequence):
        encoded_sequence, merged_node = self.huffman.huffman_encoding(sequence)

        self.assertGreater(sys.getsizeof(sequence), sys.getsizeof(sys.getsizeof(int(encoded_sequence, base=2))))

        decoded_sequence = self.huffman.huffman_decoding(encoded_sequence, merged_node)

        self.assertEqual(sys.getsizeof(decoded_sequence), sys.getsizeof(sequence))

    @parameterized.expand([
        [""],
        [" "],
        [None]
    ])
    def test_null_or_empty_sequence_cases(self, sequence):
        if sequence is not None:
            sequence = sequence.strip()

        encoded_sequence, merged_node = self.huffman.huffman_encoding(sequence)

        self.assertEqual(len(encoded_sequence), 0)

        decoded_sequence = self.huffman.huffman_decoding(encoded_sequence, merged_node)

        print("Input: ", sequence, " ,output: ", decoded_sequence)

        self.assertEqual(len(decoded_sequence), len(sequence) if sequence is not None else 0)



if __name__ == '__main__':
    unittest.main()
