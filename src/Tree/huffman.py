from collections import defaultdict

from src.Tree.heap import Heap
from src.Tree.node import HeapNode, HuffmanNode


class HuffmanTree:
    def build_huffman_tree(self, data):
        frequency = defaultdict(int)
        for char in data:
            frequency[char] += 1

        min_heap = Heap(order="min")

        for char, freq in frequency.items():
            min_heap.add(HuffmanNode(char=char, frequency=freq))

        while len(min_heap) > 1:
            left = min_heap.extract()
            right = min_heap.extract()

            merged_freq = left.frequency + right.frequency
            merged_node = HuffmanNode(char=None, frequency=merged_freq)
            merged_node.left = left
            merged_node.right = right
            min_heap.add(merged_node)

        return min_heap.extract()

    def build_huffman_codes(self, root, code='', codes=None):
        if codes is None:
            codes = {}
        if root:
            if not root.left and not root.right:
                codes[root.char] = code
            self.build_huffman_codes(root.left, code + '0', codes)
            self.build_huffman_codes(root.right, code + '1', codes)
        return codes

    def huffman_encoding(self, data):
        if not data:
            return '', None

        root = self.build_huffman_tree(data)
        codes = self.build_huffman_codes(root)

        encoded_data = ''.join(codes[char] for char in data)

        return encoded_data, root

    def huffman_decoding(self, data, tree):
        if not data or not tree:
            return ''

        decoded_data = ''
        current_node = tree

        for bit in data:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if not current_node.left and not current_node.right:
                decoded_data += current_node.char
                current_node = tree

        return decoded_data


huffman = HuffmanTree()

data = 'AAAAAAABBBCCCCCCCDDEEEEEE'

print(huffman.build_huffman_tree(data).frequency)

encoded_data, tree = huffman.huffman_encoding(data)
print("Encoded data:", encoded_data)

decoded_data = huffman.huffman_decoding(encoded_data, tree)
print("Decoded data:", decoded_data)