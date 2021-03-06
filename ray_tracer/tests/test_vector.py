import math
import unittest

from math import sqrt
from point import Point
from tuple import Tuple
from util import Utilities
from vector import Vector


class TestVector(unittest.TestCase):
    def test_create(self):
        v = Vector(4, -4, 3)
        t = Tuple(v.x, v.y, v.z, 0.0)
        self.assertTrue(v == t)

    def test_is_point(self):
        v = Vector(4, -4, 3)
        self.assertFalse(v.is_point())

    def test_is_vector(self):
        v = Vector(4, -4, 3)
        self.assertTrue(v.is_vector())

    def test_add_vector(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = v1 + v2
        self.assertTrue(v3.is_vector())
        self.assertEqual(v3, Vector(5, 7, 9))

    def test_subtract_point(self):
        with self.assertRaises(TypeError):
            Vector(1, 2, 3) - Point(4, 5, 6)

    def test_subtract_vector(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 6, 7)
        v3 = v1 - v2
        self.assertTrue(v3.is_vector())
        self.assertEqual(v3, Vector(-2, -4, -6))

    def subtract_from_zero_vector(self):
        zero = Vector(0, 0, 0)
        v1 = Vector(1, -2, 3)
        v2 = zero - v1
        self.assertTrue(v2.is_vector())
        self.assertEqual(v2, Vector(-1, 2, -3))

    def test_magnitude(self):
        self.assertTrue(Utilities.equal(Vector(1, 0, 0).magnitude(), 1))
        self.assertTrue(Utilities.equal(Vector(0, 1, 0).magnitude(), 1))
        self.assertTrue(Utilities.equal(Vector(0, 0, 1).magnitude(), 1))
        self.assertTrue(Utilities.equal(Vector(1, 2, 3).magnitude(), sqrt(14)))
        self.assertTrue(Utilities.equal(Vector(-1, -2, -3).magnitude(), sqrt(14)))

    def test_normalize(self):
        self.assertEqual(Vector(4, 0, 0).normalize(), Vector(1, 0, 0))
        self.assertEqual(Vector(1, 2, 3).normalize(), Vector(0.26726, 0.53452, 0.80178))

    def test_normalized_magnitude(self):
        self.assertTrue(
            Utilities.equal(Vector(1, 2, 3).normalize().magnitude(), 1))

    def test_dot_product(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(2, 3, 4)
        self.assertTrue(Utilities.equal(v1.dot_product(v2), 20))

    def test_cross_product(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(2, 3, 4)
        self.assertEqual(v1.cross_product(v2), Vector(-1, 2, -1))
        self.assertEqual(v2.cross_product(v1), Vector(1, -2, 1))

    def test_cross_product_with_point(self):
        with self.assertRaises(NotImplementedError):
            Vector().cross_product(Point())

    def test_reflect_flat_surface(self):
        v = Vector(x=1, y=-1, z=0)
        n = Vector(x=0, y=1, z=0)
        r = v.reflect(normal=n)
        self.assertEqual(r, Vector(x=1, y=1, z=0))

    def test_reflect_slanted_surface(self):
        v = Vector(0, -1, 0)
        n = Vector(x=math.sqrt(2)/2, y=math.sqrt(2)/2, z=0)
        r = v.reflect(normal=n)
        self.assertEqual(r, Vector(x=1, y=0, z=0))


if __name__ == '__main__':
    unittest.main()
