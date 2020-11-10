from typing import List, Tuple


def add_tax(price):
    price = round(1.06 * price, 2)
    return price


def swap(char):
    new_char = chr(ord("z") - (ord(char) - ord("a")))
    return new_char


def list_item(recipe_item, stock_item):
    how_many = recipe_item[1] - stock_item
    return f"{how_many}x {recipe_item[0]}"


def shopping_list(recipe: List[Tuple[str, int]], stock: List[int]):
    return "\n".join(map(list_item, recipe, stock))


if __name__ == '__main__':
    # Testy:
    print(shopping_list([("apple", 5), ("butter", 1), ("egg", 3)], [1, 0, 1]))
    #4x apple
    #1x butter
    #2x egg

    print("---------")
    print(shopping_list([("tomato", 6), ("tortilla", 5), ("canned beans", 2), ("chilli pepper", 2)], [3, 3, 1, 0]))
    #3x tomato
    #2x tortilla
    #1x canned beans
    #2x chilli pepper

