from src.Tree.heap import Heap
from src.Tree.huffman_coding import HuffmanTree

if __name__ == '__main__':
    print("Heap sample outputs:")
    data = 'The bird is the word'
    char_freq = {}
    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1
    print(len(char_freq.items()))
    min_heap = Heap(comparator=lambda x, y: x > y)
    for char, freq in char_freq.items():
        min_heap.add((freq, char))

    list = [(freq, char) for char, freq in char_freq.items()]
    heapq.heapify(list)

    print("Built-in min heap: ", list)

    print("Min heap traversal: ")
    print("Pre-order: ", min_heap.traverse("pre_order"))
    print("In-order: ", min_heap.traverse("in_order"))
    print("Post-order: ", min_heap.traverse("post_order"))
    print("Depth first search: ", min_heap.traverse("depth_first_search"))
    print("Breadth first search: ", min_heap.traverse("breadth_first_search"))
    print("Heap size: ", len(min_heap))

    max_heap = Heap(comparator=lambda x, y: x < y)

    for char, freq in char_freq.items():
        max_heap.add((freq, char))

    print("Max heap traversal: ")
    print("Pre-order: ", max_heap.traverse("pre_order"))
    print("In-order: ", max_heap.traverse("in_order"))
    print("Post-order: ", max_heap.traverse("post_order"))
    print("Depth first search: ", max_heap.traverse("depth_first_search"))
    print("Breadth first search: ", max_heap.traverse("breadth_first_search"))
    print("Heap size: ", len(max_heap))

    print("Huffman coding sample outputs:")

    huffman = HuffmanTree()

    sequence = 'The bird is the word'

    print(huffman.merge_nodes(sequence))

    encoded_sequence, tree = huffman.huffman_encoding(sequence)
    print("Encoded data:", encoded_sequence)

    decoded_sequence = huffman.huffman_decoding(encoded_sequence, tree)
    print("Decoded data:", decoded_sequence)

    sequence = None

    print(huffman.merge_nodes(sequence))

    encoded_sequence, tree = huffman.huffman_encoding(sequence)
    print("Encoded data:", encoded_sequence)

    decoded_sequence = huffman.huffman_decoding(encoded_sequence, tree)
    print("Decoded data:", decoded_sequence)
