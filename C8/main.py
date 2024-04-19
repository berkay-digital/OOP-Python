import unittest
from portfolio1 import Portfolio


class PortfolioTest(unittest.TestCase):

    def test_total(self):
        p = Portfolio()
        p.add(5)
        p.add(10)
        self.assertEqual(p.total(), 15)

    def test_total_empty(self):
        p = Portfolio()
        self.assertEqual(p.total(), 0)

    def test_total_negative(self):
        p = Portfolio()
        p.add(-5)
        p.add(-10)
        self.assertEqual(p.total(), -15)

    def test_total_float(self):
        p = Portfolio()
        p.add(5.5)
        p.add(10.5)
        self.assertEqual(p.total(), 16)


if __name__ == '__main__':
    unittest.main()