def pow_two(x: int) -> int:
    r = 1
    i = 0

    while i != x:
        r *= 2
        i += 1

    return r


def test_pow_two() -> None:
    assert pow_two(0) == 1
    assert pow_two(1) == 2
    assert pow_two(2) == 4
    assert pow_two(3) == 8
    assert pow_two(4) == 16
    assert pow_two(5) == 32
