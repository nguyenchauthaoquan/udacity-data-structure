import heapq

from src.Tree.node import Node


class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.root = None
        self.comparator = comparator

    def add(self, value):
        if not self.root:
            self.root = Node(value=value)
            return

        traversed = [self.root]
        while len(traversed) > 0:
            node = traversed.pop(0)

            if not node.left:
                node.left = Node(value=value)
                break
            elif not node.right:
                node.right = Node(value=value)
                break
            else:
                traversed.append(node.left)
                traversed.append(node.right)
        self._heaptify_up(value)

    def extract(self):
        if not self.root:
            return None
        current_value = self.root.value
        last_node = self._find_last_node()

        if self.root == last_node:
            self.root = None
        else:
            self.root.value = last_node.value
            self._remove_last_node()
            self._heaptify_down(self.root.value)
        return current_value

    def traverse(self, key):
        traversed_results = {
            "pre_order": self.pre_order(self.root),
            "in_order": self.in_order(self.root),
            "post_order": self.post_order(self.root),
            "depth_first_search": self.depth_first_search(),
            "breadth_first_search": self.breadth_first_search(),
        }

        return traversed_results.get(key.lower(), [])

    def pre_order(self, node):
        if not node:
            return []

        left_traversed = self.pre_order(node.left)
        right_traversed = self.pre_order(node.right)
        return [node.value] + left_traversed + right_traversed

    def in_order(self, node):
        if not node:
            return []
        left_traversed = self.in_order(node.left)
        right_traversed = self.in_order(node.right)

        return left_traversed + [node.value] + right_traversed

    def post_order(self, node):
        if not node:
            return []
        left_traversed = self.post_order(node.left)
        right_traversed = self.post_order(node.right)

        return left_traversed + right_traversed + [node.value]

    def depth_first_search(self):
        traversed = [self.root]
        results = []

        while len(traversed) > 0:
            node = traversed.pop()

            if node.left:
                traversed.append(node.left)
            if node.right:
                traversed.append(node.right)

            results.append(node.value)
        return results

    def breadth_first_search(self):
        traversed = [self.root]
        results = []

        while len(traversed) > 0:
            node = traversed.pop()

            results.append(node.value)

            if node.left:
                traversed.append(node.left)
            if node.right:
                traversed.append(node.right)
        return results

    def _heaptify_up(self, value):
        found_node = self._find_heap_node(self.root, value)

        while found_node:
            parent_node = self._find_parent_node(self.root, value)

            if parent_node and self.comparator(parent_node, found_node):
                parent_node.value, found_node.value = found_node.value, parent_node.value
                found_node = parent_node
            else:
                break

    def _heaptify_down(self, value):
        found_node = self._find_heap_node(self.root, value)

        while found_node:
            found_child_node = self._find_child_node(found_node)
            if found_child_node and found_child_node.value > found_node.value:
                found_child_node.value, found_node.value = found_node.value, found_child_node.value
                found_node = found_child_node
            else:
                break

    def _find_heap_node(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        left_node = self._find_heap_node(node.left, value)
        right_node = self._find_heap_node(node.right, value)

        return left_node if left_node else right_node

    def _find_parent_node(self, node, value):
        if not node:
            return None

        if (node.left and node.left.value == value) or (node.right and node.right.value == value):
            return node

        left_node = self._find_parent_node(node.left, value)
        right_node = self._find_parent_node(node.right, value)

        return left_node if left_node else right_node

    def _find_last_node(self):
        global node
        traversed = [self.root]

        while len(traversed) > 0:
            node = traversed.pop(0)
            if node.left:
                traversed.append(node.left)
            if node.right:
                traversed.append(node.right)
        return node

    def _find_child_node(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return None
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        return node.left if self.comparator(node.left, node.right) else node.right

    def _remove_last_node(self):
        if not self.root:
            return

        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left:
                if node.left == self._find_last_node():
                    node.left = None
                    break
                else:
                    queue.append(node.left)
            if node.right:
                if node.right == self._find_last_node():
                    node.right = None
                    break
                else:
                    queue.append(node.right)

    def _get_heap_size(self, node):
        if not node:
            return 0
        return 1 + self._get_heap_size(node.left) + self._get_heap_size(node.right)

    def __len__(self):
        return self._get_heap_size(self.root)



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
