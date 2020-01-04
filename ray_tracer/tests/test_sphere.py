import math
import unittest

from materials import Material
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

    def test_normal_on_x_axis(self):
        n = self._sphere.normal_at(position=Point(x=1, y=0, z=0))
        self.assertEqual(n, Vector(x=1, y=0, z=0))

    def test_normal_on_y_axis(self):
        n = self._sphere.normal_at(position=Point(x=0, y=1, z=0))
        self.assertEqual(n, Vector(x=0, y=1, z=0))

    def test_normal_on_z_axis(self):
        n = self._sphere.normal_at(position=Point(x=0, y=0, z=1))
        self.assertEqual(n, Vector(x=0, y=0, z=1))

    def test_normal_non_axial_point(self):
        n = self._sphere.normal_at(position=Point(x=math.sqrt(3)/3,
                                                  y=math.sqrt(3)/3,
                                                  z=math.sqrt(3)/3))
        self.assertEqual(n, Vector(x=math.sqrt(3)/3,
                                   y=math.sqrt(3)/3,
                                   z=math.sqrt(3)/3))

    def test_normal_is_normalized(self):
        n = self._sphere.normal_at(position=Point(x=math.sqrt(3) / 3,
                                                  y=math.sqrt(3) / 3,
                                                  z=math.sqrt(3) / 3))
        self.assertEqual(n, n.normalize())

    def test_normal_on_translated(self):
        self._sphere.transform = Matrix.translation_transform(x=0, y=1, z=0)
        n = self._sphere.normal_at(position=Point(x=0, y=1.70711, z=-0.70711))
        self.assertEqual(n, Vector(x=0, y=0.70711, z=-0.70711))

    def test_normal_on_scaled_and_rotated(self):
        self._sphere.transform = Matrix.scaling_transform(x=1, y=0.5, z=1) * \
                                 Matrix.rotation_z_transform(radians=math.pi/5)
        n = self._sphere.normal_at(position=Point(x=0,
                                                  y=math.sqrt(2)/2,
                                                  z=-math.sqrt(2)/2))
        self.assertEqual(n, Vector(0, 0.97014, -0.24254))

    def test_material_default(self):
        self.assertEqual(self._sphere.material, Material())

    def test_material_set(self):
        self._sphere.material = Material(ambient=1.0)
        self.assertEqual(self._sphere.material, Material(ambient=1.0))


if __name__ == '__main__':
    unittest.main()
