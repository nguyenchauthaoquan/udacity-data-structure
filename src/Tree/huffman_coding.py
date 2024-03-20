from src.Tree.heap import Heap


class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


class HuffmanTree:
    def merge_nodes(self, sequence):
        frequency = {}
        for char in sequence:
            frequency[char] = frequency.get(char, 0) + 1

        min_heap = Heap() # [HuffmanNode(char, freq) for char, freq in frequency.items()]

        for char, freq in frequency.items():
            min_heap.add(HuffmanNode(char=char, frequency=freq))

        while len(min_heap) > 1:
            left = min_heap.extract() #heapq.heappop(min_heap)
            right = min_heap.extract() #heapq.heappop(min_heap)

            merged_frequency = left.frequency + right.frequency
            merged_node = HuffmanNode(None, merged_frequency)
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

    def huffman_encoding(self, sequence):
        if not sequence:
            return '', None

        merged_node = self.merge_nodes(sequence)
        codes = self.build_huffman_codes(merged_node)

        encoded_sequence = ''.join(codes[char] for char in sequence)

        return encoded_sequence, merged_node

    def huffman_decoding(self, sequence, merged_node):
        if not sequence or not merged_node:
            return ''

        decoded_sequence = ''
        current_node = merged_node

        for bit in sequence:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if not current_node.left and not current_node.right:
                decoded_sequence += current_node.char
                current_node = merged_node

        return decoded_sequence


huffman = HuffmanTree()

sequence = 'The bird is the word'

print(huffman.merge_nodes(sequence).frequency)

encoded_sequence, tree = huffman.huffman_encoding(sequence)
print("Encoded data:", encoded_sequence)

decoded_sequence = huffman.huffman_decoding(encoded_sequence, tree)
print("Decoded data:", decoded_sequence)

sequence = 'AAAAAAABBBCCCCCCCDDEEEEEE'

print(huffman.merge_nodes(sequence).frequency)

encoded_sequence, tree = huffman.huffman_encoding(sequence)
print("Encoded data:", encoded_sequence)

decoded_sequence = huffman.huffman_decoding(encoded_sequence, tree)
print("Decoded data:", decoded_sequence)
