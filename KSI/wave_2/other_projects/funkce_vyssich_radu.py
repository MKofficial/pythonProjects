from typing import List, Optional, Dict, Callable, Any, Tuple


def swap_pair(a, b) -> tuple:
    return b, a


def get_value_at_zero(f):
    return f(1)


def identity(x):
    return x


def lin(x: int) -> float:
    return 3*x + 1


def exp2(x: int) -> int:
    return 2**x


def f(item1: Any, item2: Any, num: int) -> Callable[[Tuple[Any, Any], Dict[int, Optional[Tuple[Any, Any]]]], List[Any]]:
    return None


from typing import Callable, List


def get_roots(f: Callable[[int], int], n: int) -> List[int]:
    return [i for i in range(n + 1) if f(i) == 0]


def constant(x):
    return 0


def linear(x):
    return x - 5


def quadratic(x):
    return x**2 - 5*x + 6


if __name__ == '__main__':
    # Tests
    print(get_roots(constant, 3))  # [0, 1, 2, 3]
    print(get_roots(constant, 0))  # [0]
    print(get_roots(linear, 4))  # []
    print(get_roots(quadratic, 3))  # [2, 3]
