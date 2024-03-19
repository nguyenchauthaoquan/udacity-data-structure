import heapq
class Heap:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)
        i = len(self.items) - 1

        while self._get_parent_index(i) >= 0 and self.items[i] < self.items[self._get_parent_index(i)]:
            self.items[i], self.items[self._get_parent_index(i)] = self.items[self._get_parent_index(i)], self.items[i]
            i = self._get_parent_index(i)

    def _get_parent_index(self, i):
        return int((i - 1) / 2)

    def _get_left_child_index(self, i):
        return 2 * i + 1

    def _get_right_child_index(self, i):
        return 2 * i + 2



heap = Heap()
heap.add(3)
heap.add(2)
heap.add(15)
heap.add(5)
heap.add(4)
heap.add(45)
print(heap.items)
list = [3,2,15,5,4,45]
heapq.heapify(list)
print(list)