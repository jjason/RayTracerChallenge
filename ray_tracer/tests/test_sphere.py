import unittest

from matrix import Matrix
from point import Point
from ray import Ray
from sphere import Sphere
from util import Utilities
from vector import Vector


class TestSphere(unittest.TestCase):
    def setUp(self):
        self._sphere = Sphere()

    def test_create(self):
        self.assertEqual(self._sphere.center, Point(x=0, y=0, z=0))
        self.assertTrue(Utilities.equal(self._sphere.radius, 1))

    def test_intersect_ray_at_two_points(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 2)
        self.assertTrue(Utilities.equal(i[0].time, 4.0))
        self.assertTrue(Utilities.equal(i[1].time, 6.0))

    def test_intersect_ray_at_tangent(self):
        r = Ray(origin=Point(x=0, y=1, z=-5), direction=Vector(x=0, y=0, z=1))
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 2)
        self.assertTrue(Utilities.equal(i[0].time, 5.0))
        self.assertTrue(Utilities.equal(i[1].time, 5.0))

    def test_intersect_ray_misses(self):
        r = Ray(origin=Point(x=0, y=2, z=-5), direction=Vector(x=0, y=0, z=1))
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 0)

    def test_intersect_ray_originates_inside(self):
        r = Ray(origin=Point(x=0, y=0, z=0), direction=Vector(x=0, y=0, z=1))
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 2)
        self.assertTrue(Utilities.equal(i[0].time, -1.0))
        self.assertTrue(Utilities.equal(i[1].time, 1.0))

    def test_intersect_ray_in_front(self):
        r = Ray(origin=Point(x=0, y=0, z=5), direction=Vector(x=0, y=0, z=1))
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 2)
        self.assertTrue(Utilities.equal(i[0].time, -6.0))
        self.assertTrue(Utilities.equal(i[1].time, -4.0))

    def test_intersect_sets_object(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 2)
        self.assertIs(i[0].object, self._sphere)
        self.assertIs(i[1].object, self._sphere)

    def test_intersect_scaled(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        self._sphere.transform = Matrix.scaling_transform(x=2, y=2, z=2)
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 2)
        self.assertTrue(Utilities.equal(i[0].time, 3))
        self.assertTrue(Utilities.equal(i[1].time, 7))

    def test_intersect_translated(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        self._sphere.transform = Matrix.translation_transform(x=5, y=0, z=0)
        i = self._sphere.intersect(ray=r)
        self.assertEqual(i.count, 0)

    def test_transform_default(self):
        self.assertEqual(self._sphere.transform, Matrix.identity())

    def test_transform_set(self):
        t = Matrix.translation_transform(x=2, y=3, z=4)
        self._sphere.transform = t
        self.assertEqual(self._sphere.transform, t)


if __name__ == '__main__':
    unittest.main()
