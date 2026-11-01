import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_sum_two_positive_values(self):
        outcome = calculate(10, 7, "+")
        self.assertEqual(outcome, 17)

    def test_sum_positive_and_negative_value(self):
        outcome = calculate(-12, 4, "+")
        self.assertEqual(outcome, -8)


if __name__ == "__main__":
    unittest.main()