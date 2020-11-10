from typing import List


def is_ge_three(number: int) -> bool:
    return number >= 3


def is_kvapil(name: List[str]) -> bool:
    first, sur = name
    return sur == "Kvapil"


if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 2, 1]
    # print(list(filter(is_ge_three, arr)))
    guests = [['Matyáš', 'Petr'], ['Jindřich', 'Kvapil'], ['Ondřej', 'Kubík'], ['Xandr', 'Kvapil']]
    print(list(filter(is_kvapil, guests)))