import unittest

from util import Utilities

class TestUtilities(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(Utilities.equal(1, 1))
        self.assertTrue(Utilities.equal(1, 1.000009))
        self.assertTrue(Utilities.equal(1, 0.999999))
        self.assertFalse(Utilities.equal(1, 1.00001))
        self.assertFalse(Utilities.equal(1, 0.9999))

if __name__ == '__main__':
    unittest.main()
