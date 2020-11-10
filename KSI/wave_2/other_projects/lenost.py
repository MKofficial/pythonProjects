def is_x_divisible_by_y(x: int, y: int) -> bool:
    print(f"[debug] Test zda je cislo {x} delitelne {y}.")
    return x % y == 0


def or_example(x: int) -> bool:
    return is_x_divisible_by_y(x, 2) or is_x_divisible_by_y(x, 5)


def and_example(x: int) -> bool:
    return is_x_divisible_by_y(x, 2) and is_x_divisible_by_y(x, 5)


def any_example(something: list) -> bool:
    for x in something:
        if x:
            return True
    return False


def all_example(something: list) -> bool:
    for x in something:
        if not x:
            return False
    return True


def does_x_equal_y(x: int, y: int) -> bool:
    print(x)
    return x == y


if __name__ == '__main__':
    # is_x_divisible_by_y(10, 2) | is_x_divisible_by_y(10, 5)
    # is_x_divisible_by_y(5, 2) & is_x_divisible_by_y(5, 5)
    # or_example(10)
    # and_example(10)

    does_x_equal_y(42, 42) and does_x_equal_y(20, 50) and does_x_equal_y(46, 46) or does_x_equal_y(47, 50)
