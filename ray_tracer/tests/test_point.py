import unittest

from point import Point
from tuple import Tuple
from vector import Vector

class TestPoint(unittest.TestCase):
    def test_create(self):
        p = Point(4, -4, 3)
        t = Tuple(p.x, p.y, p.z, 1.0)
        self.assertTrue(p == t)

    def test_is_point(self):
        p = Point(4, -4, 3)
        self.assertTrue(p.is_point())

    def test_is_vector(self):
        p = Point(4, -4, 3)
        self.assertFalse(p.is_vector())

    def test_add_point(self):
        with self.assertRaises(TypeError):
            Point(1, 2, 3) + Point(4, 5, 6)

    def test_add_vector(self):
        p1 = Point(1, 2, 3)
        v = Vector(4, 5, 6)
        p2 = p1 + v
        self.assertTrue(p2.is_point())
        self.assertEqual(p2, Point(5, 7, 9))

    def test_subtract_point(self):
        p1 = Point(3, 2, 1)
        p2 = Point(5, 6, 7)
        v = p1 - p2
        self.assertTrue(v.is_vector())
        self.assertEqual(v, Vector(-2, -4, -6))

    def test_subtract_vector(self):
        p1 = Point(3, 2, 1)
        v = Vector(5, 6, 7)
        p2 = p1 - v
        self.assertTrue(p2.is_point())
        self.assertEqual(p2, Point(-2, -4, -6))

    def test_magnitude(self):
        with self.assertRaises(NotImplementedError):
            Point().magnitude()

    def test_normalize(self):
        with self.assertRaises(NotImplementedError):
            Point().normalize()

    def test_dot_product_with_point(self):
        with self.assertRaises(NotImplementedError):
            Point().dot_product(Point())

    def test_dot_product_with_vector(self):
        with self.assertRaises(NotImplementedError):
            Point().dot_product(Vector())

    def test_cross_product_with_point(self):
        with self.assertRaises(NotImplementedError):
            Point().cross_product(Point())

    def test_cross_product_with_vector(self):
        with self.assertRaises(NotImplementedError):
            Point().cross_product(Vector())



if __name__ == '__main__':
    unittest.main()
