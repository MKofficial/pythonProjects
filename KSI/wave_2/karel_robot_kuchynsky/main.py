from typing import List, Any
from inspect import signature


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
    return bowl_a + bowl_b + bowl_c


def boil(bowl: List[str]) -> List[str]:
    return [f"°{i}°" for i in bowl]


def remove(bowl_a: List[str], bowl_b: List[str]) -> List[str]:
    return [i for i in bowl_b if i not in bowl_a]


def cook(recipe: List[Any]) -> List[str]:
    functions = []  # stores functions
    ingredients = []
    index = None  # stores index of last callable element in recipe
    for i in recipe:
        if isinstance(index, int):
            if callable(i):
                ingredients.append(recipe[index + 1: recipe.index(i)])
                index = recipe.index(i)
            elif recipe.index(i) == len(recipe) - 1:
                ingredients.append(recipe[index + 1: recipe.index(i) + 1])
        if callable(i):
            functions.append(i)
            index = recipe.index(i)

    fun_and_ing = list(zip(functions, ingredients))
    # change all tuples to lists
    for i in fun_and_ing:
        fun_and_ing[fun_and_ing.index(i)] = list(i)

    while callable(fun_and_ing[0][0]):
        for i in fun_and_ing:
            if not callable(i[0]):
                fun_and_ing[fun_and_ing.index(i) - 1].append(i)
                del fun_and_ing[fun_and_ing.index(i)]
            try:
                fun_and_ing[fun_and_ing.index(i)] = i[0](*i[1:])
            except TypeError:
                continue

    pass


if __name__ == '__main__':
    print(cook([bake, ["sour cream"], cut, ["plum", "plum", "plum"], remove, ["vanilla"],
                mix, ["flour", "baking powder"], ["sugar", "eggs", "vanilla"]]))
    # print(len(signature(bake).parameters))
