import unittest

from intersections import Intersection, Intersections
from matrix import Matrix
from point import Point
from ray import Ray
from sphere import Sphere
from util import Utilities
from vector import Vector


class TestIntersection(unittest.TestCase):
    def test_create(self):
        s = Sphere()
        i = Intersection(time=3.5, the_object=s)
        self.assertEqual(i.time, 3.5)
        self.assertIs(i.the_object, s)

    def test_prepare_computations(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        s = Sphere()
        i = Intersection(time=4, the_object=s)
        c = i.prepare_computations(ray=r)
        self.assertTrue(Utilities.equal(c.time, i.time))
        self.assertIs(c.the_object, i.the_object)
        self.assertEqual(c.position, Point(x=0, y=0, z=-1))
        self.assertEqual(c.eye, Vector(x=0, y=0, z=-1))
        self.assertEqual(c.normal, Vector(x=0, y=0, z=-1))

    def test_prepare_computations_hit_outside(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        s = Sphere()
        i = Intersection(time=4, the_object=s)
        c = i.prepare_computations(ray=r)
        self.assertFalse(c.inside)

    def test_prepare_computations_hit_inside(self):
        r = Ray(origin=Point(x=0, y=0, z=0), direction=Vector(x=0, y=0, z=1))
        s = Sphere()
        i = Intersection(1, s)
        c = i.prepare_computations(ray=r)
        self.assertEqual(c.position, Point(x=0, y=0, z=1))
        self.assertEqual(c.eye, Vector(x=0, y=0, z=-1))
        self.assertTrue(c.inside)
        # Normal would _normally_ be (0, 0, 1) but is inverted
        self.assertEqual(c.normal, Vector(x=0, y=0, z=-1))


class TestIntersections(unittest.TestCase):
    def setUp(self):
        self._sphere = Sphere()

    def test_aggregating(self):
        i1 = Intersection(time=1, the_object=self._sphere)
        i2 = Intersection(time=2, the_object=self._sphere)
        ii = Intersections(i1, i2)
        self.assertEqual(ii.count, 2)
        self.assertTrue(Utilities.equal(ii[0].time, 1))
        self.assertTrue(Utilities.equal(ii[1].time, 2))

    def test_hit_all_intersections_positive(self):
        i1 = Intersection(time=1, the_object=self._sphere)
        i2 = Intersection(time=2, the_object=self._sphere)
        self.assertEqual(Intersections(i1, i2).hit(), i1)

    def test_hit_some_intersections_negative(self):
        i1 = Intersection(time=-1, the_object=self._sphere)
        i2 = Intersection(time=1, the_object=self._sphere)
        self.assertEqual(Intersections(i1, i2).hit(), i2)

    def test_hit_all_intersections_negative(self):
        i1 = Intersection(time=-2, the_object=self._sphere)
        i2 = Intersection(time=-1, the_object=self._sphere)
        self.assertIsNone(Intersections(i1, i2).hit())

    def test_hit_always_chooses_lowest_nonnegative(self):
        i1 = Intersection(time=5, the_object=self._sphere)
        i2 = Intersection(time=7, the_object=self._sphere)
        i3 = Intersection(time=-3, the_object=self._sphere)
        i4 = Intersection(time=2, the_object=self._sphere)
        self.assertEqual(Intersections(i1, i2, i3, i4).hit(), i4)

    def test_hit_should_offset_the_point(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        s = Sphere(transform=Matrix.translation_transform(x=0, y=0, z=1))
        i = Intersection(time=5, the_object=s)
        c = i.prepare_computations(ray=r)
        self.assertLess(c.over_position.z, -Utilities.EPSILON / 2)
        self.assertGreater(c.position.z, c.over_position.z)


if __name__ == '__main__':
    unittest.main()
