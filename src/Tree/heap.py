from src.Tree.node import HeapNode


class Heap:
    def __init__(self, order):
        """
        Initialize the new binary heap.
        @param order: the binary heap type ("min" represents the min heap, "max" represents the max heap)
        @raise: ValueError if order is neither "min" nor "max"
        """
        self.root = None

        if isinstance(order, str):
            if order.lower() == "min" or order.lower() == "max":
                self.order = order
            else:
                raise ValueError()
        else:
            raise TypeError()

    def add(self, value):
        if self.root is None:
            self.root = HeapNode(value)
        else:
            self._add(self.root, value)

    def extract(self):
        if not self.root:
            return None
        current_value = self.root.value
        if not self.root.left and not self.root.right:
            self.root = None
            return current_value

        last_node_value = self._remove_last_node(self.root)
        self.root.value = last_node_value
        self._heaptify_down(self.root)
        return current_value

    def pre_order(self):
        return self._pre_order(self.root)

    def _add(self, node, value):
        if not node.left:
            node.left = HeapNode(value)
            self._heaptify_up(node.left)
        elif not node.right:
            node.right = HeapNode(value)
            self._heaptify_up(node.right)
        else:
            self._add(node.left, value)

    def _heaptify_up(self, node):
        parent = self._get_parent_node(node)

        if parent and self._compare(node.value, parent.value):
            node.value, parent.value = parent.value, node.value
            self._heaptify_up(parent)

    def _heaptify_down(self, node):
        if not node:
            return
        current_node = node

        if node.left and self._compare(node.left.value, current_node.value):
            current_node = node.left
        if node.right and self._compare(node.right.value, current_node.value):
            current_node = node.right

        if current_node is not node:
            node.value, current_node.value = current_node.value, node.value
            self._heaptify_down(current_node)

    def _get_parent_node(self, node):
        if not node or node is self.root:
            return None

        current_node = self.root

        if current_node.left is node or current_node.right is node:
            return current_node
        else:
            if current_node.left:
                return current_node.left
            if current_node.right:
                return current_node.right
            return self._get_parent_node(current_node)

    def _remove_last_node(self, node):
        if not node:
            return None

        traversed = [node]

        while traversed:
            current_node = traversed.pop(0)
            parent_node = self._get_parent_node(current_node)
            if current_node.left:
                traversed.append(current_node.left)
            elif current_node.right:
                traversed.append(current_node.right)
            else:
                if parent_node:
                    if parent_node.left is current_node:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                return current_node.value

    def _compare(self, x, y):
        if self.order.lower() == "min":
            return x < y
        elif self.order.lower() == "max":
            return x > y

    def _pre_order(self, node):
        traversed = []
        if not node:
            return []

        traversed.append(node.value)
        traversed.extend(self._pre_order(node.left))
        traversed.extend(self._pre_order(node.right))

        return traversed

    def _get_tree_size(self, node):
        if not node:
            return 0
        return 1 + self._get_tree_size(node.left) + self._get_tree_size(node.right)

    def __len__(self):
        return self._get_tree_size(self.root)



# Example usage:
data = 'AAAAAAABBBCCCCCCCDDEEEEEE'
char_freq = {}
for char in data:
    char_freq[char] = char_freq.get(char, 0) + 1
print(char_freq)
min_heap = Heap(order="min")
for char, freq in char_freq.items():
    min_heap.add((freq, char))

print("Min Heap: ", min_heap.pre_order())
print(len(min_heap))
print("Extracted: ", min_heap.extract())
print("Min Heap: ", min_heap.pre_order())

max_heap = Heap(order="max")
for char, freq in char_freq.items():
    max_heap.add((freq, char))
print("Max Heap: ", max_heap.pre_order())
print(len(max_heap))
print("Extracted: ", max_heap.extract())
print("Max Heap: ", max_heap.pre_order())
