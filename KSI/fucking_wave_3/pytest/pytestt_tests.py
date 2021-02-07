import unittest

from pytestt import pow_two


class MyTestCase(unittest.TestCase):
    assert pow_two(0) == 1
    assert pow_two(1) == 2
    assert pow_two(2) == 4
    assert pow_two(3) == 8
    assert pow_two(4) == 16
    assert pow_two(5) == 32


if __name__ == '__main__':
    unittest.main()
