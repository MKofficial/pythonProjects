import math
import unittest
# example implementation of function (might not be correct)
quadratic_equation = lambda a, b, c: ((-b - math.sqrt(b*b - 4*a*c))/(2*a),
                                      ((-b + math.sqrt(b*b - 4*a*c))/(2*a)))


class QuadraticEquationTest(unittest.TestCase):
    # tests quadratic_equation method on valid inputs
    # (a not 0, all numbers)
    def test_valid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(quadratic_equation(0, 1, 1), (0, 0))
        with self.assertRaises(TypeError):
            self.assertEqual(quadratic_equation(1), (0, 0))
        with self.assertRaises(ValueError):
            self.assertEqual(type(quadratic_equation(1, 2, 2)), (0, 0))

    # tests how function reacts to invalid inputs
    # like number is not passed as arg
    def test_crazy_inputs(self):
        pass

