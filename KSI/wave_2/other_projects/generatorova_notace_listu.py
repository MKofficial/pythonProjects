from typing import List, Tuple


def color_combinations(colors: List[str]) -> List[Tuple[str, str, str]]:
    return [(i, j, k) for i in colors for j in colors for k in colors if i != j and i != k and j != k]


def matrix(n: int):
    complete = []
    diagonal_one = 0
    diagonal_two = n - 1
    # for i in range(n):
    #     one = []
    #     for j in range(n):
    #         if j == diagonal_one or j == diagonal_two:
    #             one.append(1)
    #         else:
    #             one.append(0)
    #     diagonal_one += 1
    #     diagonal_two -= 1
    #     complete.append(one)
    return [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]


if __name__ == '__main__':
    print(matrix(4))
