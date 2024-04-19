from unittest import TestCase
from number import Number


class TestNumber(TestCase):
    def test_avarage(self):
        n = Number([1, 2, 3, 4, 5])
        self.assertEqual(n.avarage(), 3)

    def test_avarage_empty(self):
        n = Number([])
        self.assertIsNone(n.avarage())

    def test_avarage_float(self):
        n = Number([1.5, 2.5, 3.5, 4.5, 5.5])
        self.assertEqual(n.avarage(), 3.5)

    def test_avarage_negative(self):
        n = Number([-1, -2, -3, -4, -5])
        self.assertEqual(n.avarage(), -3)

    def test_avarage_mixed(self):
        n = Number([1, -2, 3, -4, 5])
        self.assertEqual(n.avarage(), 0.6)

    def test_avarage_string(self):
        n = Number(['a', 'b', 'c', 'd', 'e'])
        self.assertIsNone(n.avarage())

    def test_avarage_mixed_string(self):
        n = Number([1, 'b', 3, 'd', 5])
        self.assertIsNone(n.avarage())