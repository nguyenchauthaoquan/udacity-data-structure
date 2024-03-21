import decimal


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, other):
        if isinstance(self.value, int) or isinstance(self.value, float) or isinstance(self.value, decimal.Decimal):
            return self.value < other.value
        elif isinstance(self.value, (list, tuple, set)):
            for value, other_value in zip(self.value, other.value):
                if (isinstance(value, int) or isinstance(value, float) or isinstance(value, decimal.Decimal)) and (
                        isinstance(other_value, int) or isinstance(other_value, float) or isinstance(other_value,
                                                                                                     decimal.Decimal)):
                    return value < other_value

    def __gt__(self, other):
        if isinstance(self.value, (int, float, decimal.Decimal, str)) and isinstance(other.value, (
        int, float, decimal.Decimal, str)):
            return self.value > other.value
        elif isinstance(self.value, (list, tuple, set)):
            for value, other_value in zip(self.value, other.value):
                if isinstance(value, (int, float, decimal.Decimal, str)) and isinstance(other_value, (
                int, float, decimal.Decimal, str)):
                    return value > other_value
