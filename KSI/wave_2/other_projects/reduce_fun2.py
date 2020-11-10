from typing import List, Iterable
from functools import reduce


def prod(array: List[int]) -> int:
    """
    Returns product of all items in array.
    """
    return reduce(lambda x, y: x * y, array)


def odd_sum(array: List[int]) -> int:
    """
    Count sum of all odd numbers in array.
    """
    # (x if x % 2 != 0 else 0) + (y if y % 2 != 0 else 0)
    return reduce(lambda x, y: x + y if y % 2 != 0 else x, array, 0)


def str_join(array: List[str]) -> str:
    """
    Joins all strings in array.
    """
    return reduce(lambda x, y: x + y, array)


def max_absolute_value(array: List[int]) -> int:
    """
    Returns maximal absolute value of array.
    If array is empty throws an exception.
    """
    return reduce(lambda x, y: max(abs(y), abs(x)), array)


def bst(array):
    """
    Add all items in array to binary search tree.
    You can create tree object by writing: tree = BST().
    You add item to tree by call: tree.add(item).
    """
    return reduce(lambda x, y: x.add(y), array, BST())


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None
        self.actual = None

    def _add(self, actual, key):
        if key < actual.key:
            if actual.left is None:
                actual.left = Node(key)
                actual.left.parent = actual
            else:
                self._add(actual.left, key)
        else:
            if actual.right is None:
                actual.right = Node(key)
                actual.right.parent = actual
            else:
                self._add(actual.right, key)

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add(self.root, key)
        return self


if __name__ == '__main__':
    # tests
    print(prod([2, 4, 5]))  # 40
    print(odd_sum([2, 5, -4, 3, 2, 5]))  # 5
    print(str_join(["I", "love", "KSI"]))  # "IloveKSI"
    print(max_absolute_value([-1, 2, -4, -5]))  # 4

    print(bst([1024]).root.key)  # 1024
