from src.Tree.node import Node


class Heap:
    def __init__(self, order):
        """
        Initialize the new binary heap.
        @param order: the binary heap type ("min" represents the min heap, "max" represents the max heap)
        """
        self.root = None
        self.size = 0

        if order == "min" or order == "max":
            self.order = order

    def add(self, value):
        self.size += 1
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def pre_order(self):
        self._pre_order(self.root)

    def _add(self, node, value):
        if not node.left:
            node.left = Node(value)
            self._heapify_up(node.left)
        elif not node.right:
            node.right = Node(value)
            self._heapify_up(node.right)
        else:
            self._add(node.left, value)

    def _get_parent_node(self, node):
        if not node or node is self.root:
            return None
        traversed = [self.root]

        while traversed:
            current = traversed.pop(0)

            if current.left == node or current.right == node:
                return current
            else:
                if current.left:
                    traversed.append(current.left)
                if current.right:
                    traversed.append(current.right)

    def _heapify_up(self, node):
        current = node
        while current and current != self.root:
            parent = self._get_parent_node(current)

            if self._compare(parent.value, current.value):
                parent.value, current.value = current.value, parent.value
                current = parent
            else:
                break

    def _compare(self, x, y):
        if self.order == "min":
            return x > y
        elif self.order == "max":
            return x < y

    def _pre_order(self, node):
        if not node:
            return
        print(node.value)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def __len__(self):
        return self.size


# Example usage:
data = 'AAAAAAABBBCCCCCCCDDEEEEEE'
char_freq = {}
for char in data:
    char_freq[char] = char_freq.get(char, 0) + 1
print(char_freq)
min_heap = Heap(order="min")
for char, freq in char_freq.items():
    min_heap.add((freq, char))

print("Min Heap:")
min_heap.pre_order()

max_heap = Heap(order="max")
for char, freq in char_freq.items():
    max_heap.add((freq, char))
print("\nMax Heap:")
max_heap.pre_order()
