from functools import reduce

from typing import Callable, List, Any


def my_list(iterator) -> list:  # 1b
    """
    Converts iterator to array.
    Using list function is forbidden.
    """
    return reduce(lambda x, y: x + [y], iterator, [])


def my_reverse(array: list) -> list:  # 1b
    """
    Reverse order of array elements.
    Using reverse function is forbidden.
    """
    return reduce(lambda x, y: [y] + x, array, [])


def my_sort(array: list) -> list:  # 1b
    """
    Sort array from lowest to highest element.
    Using functions to sort (like sort or sorted) is forbidden.
    """
    # recursive with adjusting array param totally
    # return reduce(lambda x, y: x + [y], array, [])


def my_map(map_function: Callable[[Any], Any], array: list) -> list:  # 1b
    """
    Apply map_function to each element of array.
    Using map function is forbidden.
    """
    return reduce(lambda x, y: x + [map_function(y)], array, [])


def is_length_odd(array: List[Any]) -> bool:  # 2b
    """
    Check whether is len(array) odd.
    Using len function is forbidden.
    """
    return reduce(lambda x, y: x + 1, array, 1) % 2 == 0


def even_numbers_only(array: List[int]) -> list:  # 2b
    """
    Filter array. Delete odd numbers. Even numbers stay in array.
    Using filter function is forbidden.
    """
    return reduce(lambda x, y: x + ([y] if y % 2 == 0 else []), array, [])


def chain_functions(array: List[Callable[[Any], Any]]) -> Callable[[Any], Any]:  # 2b
    """
    Creates new function, that is composed from all unary functions in array.
    Example: chain_functions([g, h]) should return following function.
    def f(x):
        return g(h(x))
    """
    return lambda x: reduce(lambda fun1, fun2: fun1(fun2(x)), array)


if __name__ == '__main__':
    # tests
    print(my_list(range(4)))  # [0, 1, 2, 3]
    print(my_reverse([1, 2, 3]))  # [3, 2, 1]
    print(my_sort([4, 2, 5, 1]))  # [1, 2, 4, 5]
    print(my_map(lambda x: x + 1, range(4)))  # [1, 2, 3, 4]
    print(is_length_odd([1, 2, 3]))  # True
    print(is_length_odd([None, None]))  # False
    print(even_numbers_only([3, 2, 1, 4, 2, 5]))  # [2, 4]

    # comment following lines if not implementing chain_functions
    f = chain_functions([lambda x: x + 1, lambda x: 2 * x])  # this should return lambda x: 2 * x + 1
    print(f(2))  # 5 = (2 * 2) + 1
    print(f(4))  # 9 = (2 * 4) + 1
