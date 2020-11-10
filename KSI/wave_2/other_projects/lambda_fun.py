from typing import Callable, Optional, Any, List


# f = lambda x: x + 2
# animals = ["Penguin", "Los", "Sob", "Bear"]


def twice(function):
    return lambda x: function(function(x))


def max_value(f: Callable[[int], int], g: Callable[[int], int]) -> Callable[[int], int]:
    return lambda x: f(x) if f(x) > g(x) else g(x)


def sort_by_count(lst: List[str]):
    return list.sort(key=lambda x: x.count("a"))


if __name__ == '__main__':
    print("fabslfjka".count("a"))
