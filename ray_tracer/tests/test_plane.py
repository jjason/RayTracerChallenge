import unittest

from plane import Plane
from point import Point
from ray import Ray
from util import Utilities
from vector import Vector


class TestPlane(unittest.TestCase):
    def setUp(self):
        self._plane = Plane()

    def test_normal_is_constant(self):
        p1 = Point(x=0, y=0, z=0)
        p2 = Point(x=10, y=0, z=-10)
        p3 = Point(x=-5, y=0, z=150)
        v = Vector(x=0, y=1, z=0)
        self.assertEqual(self._plane._normal_at(position=p1), v)
        self.assertEqual(self._plane._normal_at(position=p2), v)
        self.assertEqual(self._plane._normal_at(position=p3), v)

    def test_intersect_with_parallel_ray(self):
        r = Ray(origin=Point(x=0, y=10, z=0), direction=Vector(x=0, y=0, z=1))
        self.assertEqual(self._plane.intersect(ray=r).count, 0)

    def test_intersect_with_coplanar_ray(self):
        r = Ray(origin=Point(x=0, y=0, z=0), direction=Vector(x=0, y=0, z=1))
        self.assertEqual(self._plane.intersect(ray=r).count, 0)

    def test_intersect_with_ray_from_above(self):
        r = Ray(origin=Point(x=0, y=1, z=0), direction=Vector(x=0, y=-1, z=0))
        i = self._plane.intersect(ray=r)
        self.assertEqual(i.count, 1)
        self.assertTrue(Utilities.equal(i[0].time, 1))
        self.assertIs(i[0].shape, self._plane)

    def test_intersect_with_ray_from_below(self):
        r = Ray(origin=Point(x=0, y=-1, z=0), direction=Vector(x=0, y=1, z=0))
        i = self._plane.intersect(ray=r)
        self.assertEqual(i.count, 1)
        self.assertTrue(Utilities.equal(i[0].time, 1))
        self.assertIs(i[0].shape, self._plane)


if __name__ == '__main__':
    unittest.main()
