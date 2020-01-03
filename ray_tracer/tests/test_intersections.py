import unittest

from intersections import Intersection, Intersections
from sphere import Sphere
from util import Utilities


class TestIntersection(unittest.TestCase):
    def test_create(self):
        s = Sphere()
        i = Intersection(time=3.5, object=s)
        self.assertEqual(i.time, 3.5)
        self.assertIs(i.object, s)


class TestIntersections(unittest.TestCase):
    def setUp(self):
        self._sphere = Sphere()

    def test_aggregating(self):
        i1 = Intersection(time=1, object=self._sphere)
        i2 = Intersection(time=2, object=self._sphere)
        ii = Intersections(i1, i2)
        self.assertEqual(ii.count, 2)
        self.assertTrue(Utilities.equal(ii[0].time, 1))
        self.assertTrue(Utilities.equal(ii[1].time, 2))

    def test_hit_all_intersections_positive(self):
        i1 = Intersection(time=1, object=self._sphere)
        i2 = Intersection(time=2, object=self._sphere)
        self.assertEqual(Intersections(i1, i2).hit(), i1)

    def test_hit_some_intersections_negative(self):
        i1 = Intersection(time=-1, object=self._sphere)
        i2 = Intersection(time=1, object=self._sphere)
        self.assertEqual(Intersections(i1, i2).hit(), i2)

    def test_hit_all_intersections_negative(self):
        i1 = Intersection(time=-2, object=self._sphere)
        i2 = Intersection(time=-1, object=self._sphere)
        self.assertIsNone(Intersections(i1, i2).hit())

    def test_hit_always_chooses_lowest_nonnegative(self):
        i1 = Intersection(time=5, object=self._sphere)
        i2 = Intersection(time=7, object=self._sphere)
        i3 = Intersection(time=-3, object=self._sphere)
        i4 = Intersection(time=2, object=self._sphere)
        self.assertEqual(Intersections(i1, i2, i3, i4).hit(), i4)


if __name__ == '__main__':
    unittest.main()
