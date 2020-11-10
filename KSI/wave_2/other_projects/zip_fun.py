from typing import List, Tuple, Any


def scalar_product(a: List[int], b: List[int]) -> int:
    zip_ab = zip(a, b)
    suma = 0

    for pair in list(zip_ab):
        suma += (pair[0] * pair[1])

    return suma


def my_zip(a: List[Any], b: List[Any]) -> List[Tuple[Any, Any]]:
    # arr = []
    # for i in range(len(a)):
    #     arr.append((a[i], b[i]))

    # return arr
    return [(a[i], b[i]) for i in range(len(a) if len(a) < len(b) else len(b))]


if __name__ == '__main__':
    print(my_zip([1, 2, 4], [3, 4, 6, 4]))
