class HeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency
