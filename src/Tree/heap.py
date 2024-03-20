from src.Tree.node import Node


class Heap:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = Node(val)
                break
            elif not node.right:
                node.right = Node(val)
                break
            else:
                queue.append(node.left)
                queue.append(node.right)
        self._heapify_up(val)

    def extract_root(self):
        if not self.root:
            return None
        root_val = self.root.value
        last_val = self._get_last_node().value
        if self.root == self._get_last_node():
            self.root = None
        else:
            self.root.value = last_val
            self._remove_last_node()
            self._heapify_down(self.root.value)
        return root_val

    def _get_last_node(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return node

    def _remove_last_node(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left:
                if node.left == self._get_last_node():
                    node.left = None
                    break
                else:
                    queue.append(node.left)
            if node.right:
                if node.right == self._get_last_node():
                    node.right = None
                    break
                else:
                    queue.append(node.right)

    def _heapify_up(self, val):
        node = self._find_node(self.root, val)
        while node:
            parent = self._find_parent(self.root, val)
            if parent and parent.value > node.value:
                parent.value, node.value = node.value, parent.value
                node = parent
            else:
                break

    def _heapify_down(self, val):
        node = self._find_node(self.root, val)
        while node:
            min_child = self._find_min_child(node)
            if min_child and min_child.value < node.value:
                min_child.value, node.value = node.value, min_child.value
                node = min_child
            else:
                break

    def _find_node(self, root, val):
        if not root:
            return None
        if root.value == val:
            return root
        left_search = self._find_node(root.left, val)
        right_search = self._find_node(root.right, val)
        return left_search if left_search else right_search

    def _find_parent(self, root, val):
        if not root:
            return None
        if (root.left and root.left.value == val) or (root.right and root.right.value == val):
            return root
        left_search = self._find_parent(root.left, val)
        right_search = self._find_parent(root.right, val)
        return left_search if left_search else right_search

    def _find_min_child(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return None
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        return node.left if node.left.value < node.right.value else node.right

    def traverse(self):
        self.pre_order(self.root)

    def pre_order(self, node):
        if node:
            print(str(node.value))
            self.pre_order(node.left)
            self.pre_order(node.right)
        else:
            return


data = 'The bird is the word'
char_freq = {}
for char in data:
    char_freq[char] = char_freq.get(char, 0) + 1
print(char_freq)
min_heap = Heap()
for char, freq in char_freq.items():
    min_heap.add((freq, char))

min_heap.traverse()

print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
print("Extracted: ", min_heap.extract_root())
