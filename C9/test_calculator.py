import unittest
from C9.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition_of_two_numbers(self):
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8)

    def test_division_of_two_numbers(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_division_by_zero_raises_exception(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

    def test_average_of_two_numbers(self):
        result = self.calculator.average(4, 2)
        self.assertEqual(result, 3)

    def test_pythagoras_theorem_calculates_hypotenuse(self):
        result = self.calculator.calculate_c_in_triangle(3, 4)
        self.assertEqual(result, 5)

    def test_quadratic_formula_calculates_zero_of_parabolic_function(self):
        result = self.calculator.calculate_zero_of_the_parabolic_function(1, -3, 2)
        self.assertEqual(result, 2)
