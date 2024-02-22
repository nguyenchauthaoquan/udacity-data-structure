from src.Tree.node import Node


class Heap:
    def __init__(self, order):
        self.root = None
        self.size = 0

        if order == "min" or order == "max":
            self.order = order

    def add(self, value):
        self.size += 1
        if self.root is None:
            self.root = Node(value)
        else:

            new_node = Node(value)
            queue = [self.root]

            while queue:
                current = queue.pop(0)
                if not current.left:
                    current.left = new_node
                    break
                elif not current.right:
                    current.right = new_node
                    break
                else:
                    queue.append(current.left)
                    queue.append(current.right)
            self._heapify_up(new_node)

    def pre_order(self):
        self._pre_order(self.root)

    def _get_parent_node(self, node):
        if node is self.root:
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


if __name__ == "__main__":
    print("Min heap")
    min_heap = Heap(order="min")
    min_heap.add(5)
    min_heap.add(7)
    min_heap.add(9)
    min_heap.add(1)
    min_heap.add(3)
    min_heap.pre_order()
    print("Heap length: ", len(min_heap))
    print("Max heap")
    max_heap = Heap(order="max")
    max_heap.add(1)
    max_heap.add(2)
    max_heap.add(3)
    max_heap.add(4)
    max_heap.pre_order()
    print("Heap length: ", len(max_heap))
