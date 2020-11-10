#!/usr/bin/python3.7

from typing import List, Any


def fibonacciGenerator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def generatorConnector(generatorsList: List[Any]):
    for generator in generatorsList:
        for element in generator:
            yield element


def passwordGenerator(length: int):
    # same numbers
    generated_numbers = []
    for i in range(10):
        str_to_return = f"{i}" * length
        generated_numbers.append(str_to_return)
        yield str_to_return

    # number before less of 1 than current
    for i in range(11 - length):
        str_to_return = "".join([f"{i + j}" for j in range(length)])
        generated_numbers.append(str_to_return)
        yield str_to_return

    # number before more of 1 than current
    for i in range(11 - length):
        str_to_return = "".join([f"{i + j}" for j in range(length - 1, -1, -1)])
        generated_numbers.append(str_to_return)
        yield str_to_return

    # other numbers
    for i in range(int("9" * length) + 1):
        str_to_return = "0" * (length - len(str(i))) + str(i)
        if str_to_return not in generated_numbers:
            yield str_to_return


def generatorOfGenerators():
    number = 1
    while True:
        yield helpful_fun(number)
        number += 1


# todo: use generator notation, not function
def helpful_fun(number: int):
    coefficient = 1
    while True:
        yield number * coefficient
        coefficient += 1


def primesGenerator():
    prime = 2
    while True:
        yield prime

        # find next prime number
        next_number = prime + 1
        while True:
            flag = True
            for i in range(2, next_number):
                if next_number % i == 0:
                    flag = False

            if flag:
                prime = next_number
                break

            next_number += 1
