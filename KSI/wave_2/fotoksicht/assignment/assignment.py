from functools import reduce
from typing import Callable, Any, List

"""
fotoksicht poskytuje nasledujici funkce:
1. load(path)
Nacte obrazek ze souboru 'path' a vrati dvourozmerny seznam hodnot barev.
K dispozici jsou obrazky ve slozce /images. Pokud chcete upravovat vlastni obrazky, musite je prekonvertovat do 8-bitoveho grayscale formatu v nejakem beznem grafickem editoru.
Priklad pouziti: img = fk.load("images/monalisa.png")

2. save(image, path)
Ulozi dvourozmerny seznam do souboru definovaneho argumentem 'path'
Priklad pouziti: fk.save(img, "images/monalisa2.png")

3. show(image)
Otevre obrazek k prohlizeni.
Priklad pouziti: fk.show(img)
"""

"""
Tvou ulohou bude v tomto zadani implementovat nasledujici funkce pomoci
funkci `map`, `filter`, `reduce` a `zip` a list comprehensions.
"""


# Aplikuje funkci 'func' na kazdy pixel (polozku v dvourozmernem seznamu) obrazku 'image' a vysledek operace vrati.
# Priklad: img = immap(lambda x: x + 1, [[1, 2], [3, 4]]) # img = [[2, 3], [4, 5]]
def immap(func: Callable[[Any], Any], image: List[List[int]]) -> List[List[int]]:
    return [[func(element) for element in inner] for inner in image]


# Aplikuje filter na radky obrazku 'image' a vysledek vrati.
# Tedy pokud radek v obrazku nesplnuje podminku 'condition', tak je smazan.
# Priklad: img = imfilterRows(lambda x: sum(x) == 0, [[0, 0], [0, 1]]) # img = [[0, 0]]
def imfilterRows(condition: Callable[[Any], Any], image: List[List[int]]) -> List[List[int]]:
    return list(filter(condition, [inner_list for inner_list in image]))


# Zameni radky za sloupce v obrazku 'image' a vysledek vrati.
# Priklad: img = imtranspose([[1, 2], [3, 4]]) # img = [[1, 3], [2, 4]]
def imtranspose(image: List[List[int]]) -> List[List[int]]:
    return [[image[column][row] for column in range(len(image))] for row in range(len(image[0]))]


# Aplikuje filter na sloupce obrazku 'image' a vysledek vrati.
# Tedy pokud sloupec v obrazku nesplnuje podminku 'condition', tak je smazan.
# Priklad: img = imfilterColumns(lambda x: sum(x) == 1, [[0, 0], [0, 1]]) # img = [[0], [1]]
def imfilterColumns(condition: Callable[[Any], Any], image: List[List[int]]) -> List[List[int]]:
    return imfilterRows(condition, imtranspose(image))
    # todo: not sure about this


# Redukuje kazdy radek obrazku 'image' pomoci funkce 'reduce' a vrati vysledek.
# Priklad: img = imreduceWidth(lambda x,y: x+y, [[1, 2], [3, 4]]) # img = [[3], [7]]
def imreduceWidth(func: Callable[[Any, Any], Any], image: List[List[int]]) -> List[List[int]]:
    return [[reduce(func, row)] for row in image]


# Redukuje kazdy sloupec obrazku 'image' na jeden radek pomoci funkce 'reduce' a vrati vysledek.
# Priklad: img = imreduceHeight(lambda x,y: x+y, [[1, 2], [3, 4]]) # img = [4, 6]
def imreduceHeight(func: Callable[[Any, Any], Any], image: List[List[int]]) -> List[int]:
    return [inner_element for outer_element in imreduceWidth(func, imtranspose(image)) for inner_element in
            outer_element]


# Redukuje kazdy sloupec obrazku 'image' a nasledne kazdy radek pomoci funkce 'reduce' a vrati vysledek.
# Priklad: img = imreduce(lambda x,y: x+y, [[1, 2], [3, 4]]) # img = [10]
def imreduce(func: Callable[[Any, Any], Any], image: List[List[int]]) -> List[int]:
    cols = imreduceHeight(func, image)
    return [reduce(func, [inner for outer in cols for inner in outer])]


# Spoji obrazky 'image1' a 'image2' pomoci funkce 'func' a vrati vysledek.
# Spojeni je definovane tak, ze novemu obrazku na pozici x, y priradi hodnotu func(image1[x][y], image2[x][y])
# Priklad: img = imzipWith(lambda xy: xy[0] + xy[1], [[1, 2], [3, 4]], [[1, 1], [2, 2]]) # img = [[2, 3], [5, 6]]
def imzipWith(func: Callable[[Any], Any], image1: List[List[int]], image2: List[List[int]]) -> List[List[int]]:
    a = list(zip([j for i in image1 for j in i], [j for i in image2 for j in i]))
    pass


# Vlozi pruhledne logo 'logo' do obrazku 'image' s nastavenou pruhlednosti 'opacity' v rozmezi 0 az 1.
# Kde 0 je uplne pruhledne a 1 je nepruhledne.
# Viz priklad vysledku v 'images/turing-logo.png' (vysledek funkci v mainu).
# Pozor! na preteceni hodnoty 255!
def addLogo(image, logo, opacity):
    pass


if __name__ == "__main__":
    # img = fk.load('images/turing.png')
    # logo = fk.load('images/logofi.png')
    # img = addLogo(img, logo, 0.1)
    # fk.save(img, 'images/turing-logo.png')
    print(imreduceHeight(lambda x, y: x + y, [[1, 2], [3, 4]]))
    pass
