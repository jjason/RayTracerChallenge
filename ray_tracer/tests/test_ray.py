import unittest

from matrix import Matrix
from point import Point
from vector import Vector
from ray import Ray


class TestRay(unittest.TestCase):
    def test_create(self):
        o = Point(x=1, y=2, z=3)
        d = Vector(x=4, y=5, z=6)
        r = Ray(origin=o, direction=d)
        self.assertEqual(r.origin, o)
        self.assertEqual(r.direction, d)

    def test_position(self):
        r = Ray(origin=Point(x=2, y=3, z=4), direction=Vector(x=1, y=0, z=0))
        self.assertEqual(r.position(time=0), Point(x=2, y=3, z=4))
        self.assertEqual(r.position(time=1), Point(x=3, y=3, z=4))
        self.assertEqual(r.position(time=-1), Point(x=1, y=3, z=4))
        self.assertEqual(r.position(time=2.5), Point(x=4.5, y=3, z=4))

    def test_transform_by_identity(self):
        r1 = Ray(origin=Point(x=1, y=2, z=3), direction=Vector(x=0, y=1, z=0))
        m = Matrix.identity()
        r2 = r1.transform(transformation=m)
        self.assertIsNot(r1, r2)
        self.assertEqual(r2.origin, r1.origin)
        self.assertEqual(r2.direction, r1.direction)

    def test_transform_by_translation(self):
        r1 = Ray(origin=Point(x=1, y=2, z=3), direction=Vector(x=0, y=1, z=0))
        m = Matrix.translate_transform(x=3, y=4, z=5)
        r2 = r1.transform(transformation=m)
        self.assertIsNot(r1, r2)
        self.assertEqual(r2.origin, Point(x=4, y=6, z=8))
        self.assertEqual(r2.direction, Vector(x=0, y=1, z=0))

    def test_transform_by_scaling(self):
        r1 = Ray(origin=Point(x=1, y=2, z=3), direction=Vector(x=0, y=1, z=0))
        m = Matrix.scale_transform(x=2, y=3, z=4)
        r2 = r1.transform(transformation=m)
        self.assertIsNot(r1, r2)
        self.assertEqual(r2.origin, Point(x=2, y=6, z=12))
        self.assertEqual(r2.direction, Vector(x=0, y=3, z=0))


if __name__ == '__main__':
    unittest.main()
