import heapq


class PriorityQueue:
    def __init__(self, order, items=None):
        if items is None:
            items = []

        self.items = []
        self.order = order
        self.comparator = lambda x, y: self._compare(x,y)

        if len(items) > 0:
            for item in items:
                self.add(item)

    def add(self, value):
        self.items.append(value)
        self._heaptify_up(len(self.items) - 1)

    def extract(self):
        if len(self.items) == 0:
            return None
        if len(self.items) == 1:
            return self.items.pop()

        min_val = self.items[0]
        self.items[0] = self.items.pop()
        self._heaptify_down(0)
        return min_val

    def _heaptify_up(self, i):
        while self._get_parent_index(i) >= 0 and self.comparator(self.items[i],self.items[self._get_parent_index(i)]):
            self.items[i], self.items[self._get_parent_index(i)] = self.items[self._get_parent_index(i)], self.items[i]
            i = self._get_parent_index(i)

    def _heaptify_down(self, i):
        left_child_index = self._get_left_child_index(i)
        right_child_index = self._get_right_child_index(i)
        smallest = i

        if left_child_index < len(self.items) and self.comparator(self.items[left_child_index], self.items[smallest]):
            smallest = left_child_index
        if right_child_index < len(self.items) and self.comparator(self.items[right_child_index],self.items[smallest]):
            smallest = right_child_index

        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self._heaptify_down(smallest)


    def _get_parent_index(self, i):
        return int((i - 1) / 2)

    def _get_left_child_index(self, i):
        return 2 * i + 1

    def _get_right_child_index(self, i):
        return 2 * i + 2

    def _compare(self, x, y):
        if self.order.lower() == "min":
            return x < y
        elif self.order.lower() == "max":
            return x > y


heap = PriorityQueue(order="min")
heap.add(7)
heap.add(3)
heap.add(7)
heap.add(2)
heap.add(6)
print(heap.items)
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.items)
heap2 = PriorityQueue(items=[7,3,7,2,6], order="max")
print(heap2.items)
print(heap2.extract())
print(heap2.extract())
print(heap2.extract())
print(heap2.extract())
print(heap2.extract())
print(heap2.items)
