import itertools


def photo_orders(heights):
    correct = []
    for permutation in itertools.permutations(heights):
        flag = True
        for index in range(len(permutation) - 1):
            if permutation[index] + 1 == permutation[index + 1] or permutation[index] - 1 == permutation[index + 1]:
                flag = False
                break

        if flag:
            correct.append(permutation)

    return correct


def buy_fish(pack_sizes, buy, min_fish):
    correct = []
    for i in itertools.combinations(pack_sizes, buy):
        if sum(i) >= min_fish:
            correct.append(i)
    return len(correct)


print(buy_fish([8, 1, 3], 2, 7))  # 2
print(buy_fish([8, 4, 5, 6], 2, 9))  # 6
