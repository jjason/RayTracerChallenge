import math
import unittest
from unittest import mock

from intersections import Intersections
from materials import Material
from matrix import Matrix
from point import Point
from ray import Ray
from shape import Shape
from vector import Vector


class TestShape(unittest.TestCase):
    def setUp(self):
        self._shape = Shape()

    def test_transform_default(self):
        self.assertEqual(self._shape.transform, Matrix.identity())

    def test_transform_set(self):
        t = Matrix.translation_transform(x=2, y=3, z=4)
        self._shape.transform = t
        self.assertEqual(self._shape.transform, t)

    def test_material_default(self):
        self.assertEqual(self._shape.material, Material())

    def test_material_set(self):
        self._shape.material = Material(ambient=1.0)
        self.assertEqual(self._shape.material, Material(ambient=1.0))

    def test_intersect_raises_excpetion(self):
        r = Ray(origin=Point(x=0, y= 0, z=-5), direction=Vector(x=0, y=0, z=1))
        with self.assertRaises(NotImplementedError):
            self._shape.intersect(ray=r)

    def test_intersect_scaled_shape_with_ray(self):
        self._shape.transform = Matrix.scaling_transform(x=2, y=2, z=2)

        # Replace the base Shape class _intersect method that is to be
        # overridden by derived classes with a MagicMock so we can see if the
        # base class delegates to the derived class _after_ it the ray has been
        # transformed.
        self._shape._intersect = mock.MagicMock(return_value=Intersections())

        r = Ray(origin=Point(x=0, y= 0, z=-5), direction=Vector(x=0, y=0, z=1))
        self._shape.intersect(ray=r)
        xr = Ray(origin=Point(x=0, y=0, z=-2.5), direction=Vector(x=0,
                                                                  y=0,
                                                                  z=0.5))
        self._shape._intersect.assert_called_with(ray=xr)

    def test_intersect_translated_shape_with_ray(self):
        self._shape.transform = Matrix.translation_transform(x=5, y=0, z=0)

        # Replace the base Shape class _intersect method that is to be
        # overridden by derived classes with a MagicMock so we can see if the
        # base class delegates to the derived class _after_ it the ray has been
        # transformed.
        self._shape._intersect = mock.MagicMock(return_value=Intersections())

        r = Ray(origin=Point(x=0, y= 0, z=-5), direction=Vector(x=0, y=0, z=1))
        self._shape.intersect(ray=r)
        xr = Ray(origin=Point(x=-5, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        self._shape._intersect.assert_called_with(ray=xr)

    def test_normal_at_raises_excpetion(self):
        with self.assertRaises(NotImplementedError):
            self._shape.normal_at(position=Point(x=0, y=1.70711, z=-0.70711))

    def test_normal_at_on_translate_shape(self):
        self._shape.transform = Matrix.translation_transform(x=0, y=1, z=0)

        # Replace the base Shape class _normal_at method that is to be
        # overridden by derived classes with a MagicMock so we can see if the
        # base class delegates to the derived class _after_ it the point has
        # been transformed.
        self._shape._normal_at = mock.MagicMock(return_value=Vector(x=0,
                                                                    y=0,
                                                                    z=-1))

        self._shape.normal_at(position=Point(x=0, y=1.70711, z=-0.70711))
        xp = Point(x=0, y=0.70711, z=-0.70711)
        self._shape._normal_at.assert_called_with(position=xp)

    def test_normal_at_on_transformed_shape(self):
        self._shape.transform = Matrix.scaling_transform(x=1, y=0.5, z=1) * \
                                Matrix.rotation_z_transform(radians=math.pi/5)

        # Replace the base Shape class _normal_at method that is to be
        # overridden by derived classes with a MagicMock so we can see if the
        # base class delegates to the derived class _after_ it the point has
        # been transformed.
        self._shape._normal_at = mock.MagicMock(return_value=Vector(x=0,
                                                                    y=0,
                                                                    z=-1))

        self._shape.normal_at(position=Point(x=0,
                                             y=math.sqrt(2)/2,
                                             z=-math.sqrt(2)/2))
        xp = Point(x=0.83125, y=1.14412, z=-0.70711)
        self._shape._normal_at.assert_called_with(position=xp)


if __name__ == '__main__':
    unittest.main()
