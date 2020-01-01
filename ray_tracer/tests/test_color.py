import unittest

from color import Color
from util import Utilities

class TestColor(unittest.TestCase):
    def test_create(self):
        c = Color(red=-0.5, green=0.4, blue=1.7)
        self.assertTrue(Utilities.equal(c.red, -0.5))
        self.assertTrue(Utilities.equal(c.green, 0.4))
        self.assertTrue(Utilities.equal(c.blue, 1.7))

    def test_add(self):
        c1 = Color(red=0.9, green=0.6, blue=0.75)
        c2 = Color(red=0.7, green=0.1, blue=0.25)
        self.assertEqual(c1 + c2, Color(red=1.6, green=0.7, blue=1.0))

    def test_subtract(self):
        c1 = Color(red=0.9, green=0.6, blue=0.75)
        c2 = Color(red=0.7, green=0.1, blue=0.25)
        self.assertEqual(c1 - c2, Color(red=0.2, green=0.5, blue=0.5))

    def test_scalar_multiply(self):
        self.assertEqual(Color(red=0.2, green=0.3, blue=0.4) * 2,
                         Color(red=0.4, green=0.6, blue=0.8))

    def test_hadamard_product(self):
        c1 = Color(red=1, green=0.2, blue=0.4)
        c2 = Color(red=0.9, green=1, blue=0.1)
        self.assertEqual(c1 * c2, Color(red=0.9, green=0.2, blue=0.04))

if __name__ == '__main__':
    unittest.main()
