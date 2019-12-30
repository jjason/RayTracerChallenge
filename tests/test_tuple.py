import unittest

from tuple import Tuple
from util import Utilities

class TestTuple(unittest.TestCase):
    def test_create(self):
        t = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertTrue(Utilities.equal(t.x, 4.3))
        self.assertTrue(Utilities.equal(t.y, -4.2))
        self.assertTrue(Utilities.equal(t.z, 3.1))
        self.assertTrue(Utilities.equal(t.w, 1.0))

    def test_is_point(self):
        t = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertTrue(t.is_point())
        self.assertFalse(t.is_vector())

    def test_is_vector(self):
        t = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertFalse(t.is_point())
        self.assertTrue(t.is_vector())

    def test_equal(self):
        t1 = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertTrue(t1 == t1)

        t2 = Tuple(t1.x, t1.y, t1.z, t1.w)
        self.assertTrue(t1 == t2)
        self.assertTrue(t2 == t1)

        t2.x = t1.x + 1.0
        self.assertFalse(t1 == t2)

        t2.x = t1.x
        t2.y = t1.y + 1.0
        self.assertFalse(t1 == t2)

        t2.y = t1.y
        t2.z = t1.z + 1.0
        self.assertFalse(t1 == t2)

        t2.z = t1.z
        t2.w = t1.w + 1.0
        self.assertFalse(t1 == t2)

    def test_not_euqal(self):
        t1 = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertFalse(t1 != t1)

        t2 = Tuple(t1.x, t1.y, t1.z, t1.w)
        self.assertFalse(t1 != t2)
        self.assertFalse(t2 != t1)

        t2.x = t1.x + 1.0
        self.assertTrue(t1 != t2)

        t2.x = t1.x
        t2.y = t1.y + 1.0
        self.assertTrue(t1 != t2)

        t2.y = t1.y
        t2.z = t1.z + 1.0
        self.assertTrue(t1 != t2)

        t2.z = t1.z
        t2.w = t1.w + 1.0
        self.assertTrue(t1 != t2)

    def test_add(self):
        t = Tuple(3, -2, 5, 1) + Tuple(-2, 3, 1, 0)
        self.assertEqual(t, Tuple(1, 1, 6, 1))

    def test_negate(self):
        self.assertEqual(-Tuple(1, -2, 3, -4), Tuple(-1, 2, -3, 4))

    def test_multiply_by_scalar(self):
        t = Tuple(1, -2, 3, -4)
        self.assertEqual(t * 3.5, Tuple(3.5, -7, 10.5, -14))
        self.assertEqual(t * 0.5, Tuple(0.5, -1, 1.5, -2))

    def test_divide_by_scalar(self):
        t = Tuple(1, -2, 3, -4)
        self.assertEqual(t / 2, Tuple(0.5, -1, 1.5, -2))

if __name__ == '__main__':
    unittest.main()
