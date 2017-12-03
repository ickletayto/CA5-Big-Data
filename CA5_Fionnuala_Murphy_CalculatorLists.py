import unittest #to allow testing
import math #brings in math functionality not native to basic python
import numpy as np
import pandas as py

class Calculator(object):

    # allows for addition of a list of numbers. e
    def add(self, values):
       return reduce(lambda x, y: x+y, values)

    # allows for subtraction of a list of numbers.
    def subtract(self, values):
       return reduce(lambda x, y: x-y, values)

    # allows for multiplication of a list of numbers.
    def multiply(self, values):
       return reduce(lambda x, y: x*y, values)

    # allows for division of a list of numbers.
    def divide(self, values):
       return reduce(lambda x, y: x/y, values)

    # allows for squaring of numbers in a list of numbers.
    def square(self, values):
        return map(lambda x: x ** 2, values)
    # allows for cubing numbers in a list of numbers.
    def cube(self, values):
        return map(lambda x: x ** 3, values)
    # allows for taking the first element in a list and increasing it to the power of subsequent numbers in the list.
    def exponential(self, values):
       return reduce(lambda x, y: x**y, values)

    # allows for taking the first element in a list and increasing it to the power of subsequent numbers in the list.
    def sqrt(self, values):
       return reduce(lambda x, y: x + math.sqrt(y), values)
    # allows for taking the first element in a list and increasing it to the power of subsequent numbers in the list.

    # allows for getting the factorieal of each number in a list of numbers.
    def factorial(self, values):
        return map(lambda x: math.factorial(x), values)
    # allows for getting the sin of each number in a list of numbers.
    def sin(self, values):
        return map(lambda x: math.sin(x), values)
    # allows for getting the cos of each number in a list of numbers.
    def cos(self, values):
        return map(lambda x: math.cos(x), values)
    # allows for getting the tan of each number in a list of numbers.
    def tan(self, values):
        return map(lambda x: math.tan(x), values)

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add([2,3,3,4])
        self.assertEqual(12, result)
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract([2,3,3,4])
        self.assertEqual(-8, result)
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply([2,3,3,4])
        self.assertEqual(72, result)
        result = self.calc.multiply([2, -3, 3, 4])
        self.assertEqual(-72, result)
        result = self.calc.multiply([2, -3, 3, -4])
        self.assertEqual(72, result)
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide([100, 2, 5, 3])
        self.assertEqual(3, result)
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square([2, 4, 5, 6])
        self.assertEqual([4, 16, 25, 36], result)
    def test_calculator_cube_method_returns_correct_result(self):
        result = self.calc.cube([2, 4, 5, 6])
        self.assertEqual([8, 64, 125, 216], result)
    def test_calculator_exponential_method_returns_correct_result(self):
        result = self.calc.exponential([2,3,3])
        self.assertEqual(512, result)
    def test_calculator_sqrt_method_returns_correct_result(self):
        result = self.calc.sqrt([2,3,3])
        self.assertEqual(5.464101615137754, result)
    def test_calculator_factorial_method_returns_correct_result(self):
        result = self.calc.factorial([2,3,3])
        self.assertEqual([2,6,6], result)
    def test_calculator_sin_method_returns_correct_result(self):
        result = self.calc.sin([2,3,3])
        self.assertEqual([0.9092974268256817, 0.1411200080598672, 0.1411200080598672], result)
    def test_calculator_cos_method_returns_correct_result(self):
        result = self.calc.cos([2,3,3])
        self.assertEqual([-0.4161468365471424, -0.9899924966004454, -0.9899924966004454], result)
    def test_calculator_tan_method_returns_correct_result(self):
        result = self.calc.tan([2,3,3])
        self.assertEqual([-2.185039863261519, -0.1425465430742778, -0.1425465430742778], result)

if __name__ == '__main__':

    unittest.main()
