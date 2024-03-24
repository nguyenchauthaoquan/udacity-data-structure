class PriorityQueue:
    def __init__(self, comparator=lambda x, y: x < y, items=None):
        """
        Initialize a priority queue with the given comparator
        @param comparator: a comparator
        @param items: The initialized priority queue items
        """
        if items is None:
            items = []

        self.items = []
        self.comparator = comparator

        if len(items) > 0:
            for item in items:
                self.add(item)

    def add(self, value):
        """
        Add the new item to the priority queue
        @param value: The item to add
        """
        self.items.append(value)
        self._heaptify_up(len(self.items) - 1)

    def extract(self):
        """
        Extracts and removes the item from the priority queue
        """
        if len(self.items) == 0:
            return None
        if len(self.items) == 1:
            return self.items.pop()

        min_val = self.items[0]
        self.items[0] = self.items.pop()
        self._heaptify_down(0)
        return min_val

    def _heaptify_up(self, i):
        """
        Bubble up the items in priority queue
        @param i: The index of the item to bubble up
        """
        while self._get_parent_index(i) >= 0 and self.comparator(self.items[i], self.items[self._get_parent_index(i)]):
            self.items[i], self.items[self._get_parent_index(i)] = self.items[self._get_parent_index(i)], self.items[i]
            i = self._get_parent_index(i)

    def _heaptify_down(self, i):
        """
        Bubble down the items in priority queue
        @param i: The index of the item to bubble down
        """
        left_child_index = self._get_left_child_index(i)
        right_child_index = self._get_right_child_index(i)
        smallest = i

        if left_child_index < len(self.items) and self.comparator(self.items[left_child_index], self.items[smallest]):
            smallest = left_child_index
        if right_child_index < len(self.items) and self.comparator(self.items[right_child_index], self.items[smallest]):
            smallest = right_child_index

        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self._heaptify_down(smallest)

    def _get_parent_index(self, i):
        """
        Gets the index of the parent item of priority queue
        @param i: The index of the item
        """
        return int((i - 1) / 2)

    def _get_left_child_index(self, i):
        """
        Gets the index of the left child item of priority queue
        @param i: The index of the item
        """
        return 2 * i + 1

    def _get_right_child_index(self, i):
        """
        Gets the index of the right child item of priority queue
        @param i: The index of the item
        """
        return 2 * i + 2
