from typing import List, Any


def add(bowl_a: List[str], bowl_b: List[str]) -> List[str]:
    array = []

    for i in bowl_a:
        array.append(i)
    for j in bowl_b:
        array.append(j)

    return array


def mix(bowl_a: List[str], bowl_b: List[str]) -> List[str]:
    array = []
    # TODO: change this code not to use exception, think about list comprehension
    for i in range(len(bowl_a)):

        try:
            array.append(bowl_a[i])
        except IndexError:
            pass

        try:
            array.append(bowl_b[i])
        except IndexError:
            pass

    return array


def cut(bowl: List[str]) -> List[str]:
    return [elem[i:i + 2] for elem in bowl for i in range(0, len(elem), 2)]


def bake(bowl_a: List[str], bowl_b: List[str], bowl_c: List[str]) -> List[str]:
    # todo: can be improved
    if len(bowl_b) > len(bowl_a):
        bowl_a = bowl_a * len(bowl_b)

    bowl_a = bowl_a[:len(bowl_b)]
    return bowl_a + bowl_b + bowl_c


def boil(bowl: List[str]) -> List[str]:
    return [f"°{i}°" for i in bowl]


def remove(bowl_a: List[str], bowl_b: List[str]) -> List[str]:
    return [i for i in bowl_b if i not in bowl_a]


def cook(recipe: List[Any]) -> List[str]:
    while callable(recipe[0]):
        for element in recipe:
            if callable(element):
                index = recipe.index(element)  # index of the first function
                index2 = len(recipe)

                for next_function in recipe[index + 1:]:
                    if callable(next_function):
                        index2 = recipe.index(next_function)  # index of next function
                        break

                param = recipe[index + 1: index2]  # parameters between the first and the second function

                try:
                    result = element(*param)
                    del recipe[index:index2]

                    # todo: figure out some better outcome than this, problem with deleting items and uploading new one
                    recipe[index] = result

                except TypeError:
                    continue


    return recipe

if __name__ == '__main__':
    pass
    print(cook([bake, ["sour cream"], cut, ["plum", "plum", "plum"], remove, ["vanilla"], mix, ["flour", "baking powder"],
          ["sugar", "eggs", "vanilla"]]))
