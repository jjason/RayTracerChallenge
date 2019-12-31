import unittest

from color import Color
from util import Utilities

class TestColor(unittest.TestCase):
    def test_create(self):
        c = Color(-0.5, 0.4, 1.7)
        self.assertTrue(Utilities.equal(c.red, -0.5))
        self.assertTrue(Utilities.equal(c.blue, 0.4))
        self.assertTrue(Utilities.equal(c.green, 1.7))

    def test_add(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 + c2, Color(1.6, 0.7, 1.0))

    def test_subtract(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        self.assertEqual(c1 - c2, Color(0.2, 0.5, 0.5))

    def test_scalar_multiply(self):
        self.assertEqual(Color(0.2, 0.3, 0.4) * 2, Color(0.4, 0.6, 0.8))

    def test_hadamard_product(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        self.assertEqual(c1 * c2, Color(0.9, 0.2, 0.04))

if __name__ == '__main__':
    unittest.main()
