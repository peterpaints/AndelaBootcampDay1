import unittest
from loan_calc import loan_calculator

class loanCalc(unittest.TestCase):
    def test_it_works(self):
        self.assertEqual(loan_calculator(100000, 12, 12), 112000)

    def test_months_less_than_13(self):
        self.assertTrue(1 <= T <= 12)
