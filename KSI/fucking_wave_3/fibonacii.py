def fibonacci_sequence(num: int) -> int:
    assert num >= 0
    a = 0
    b = 1

    for i in range(num):
        x = a
        a += b
        b += x

    return a