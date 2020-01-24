import unittest

from color import Color
from matrix import Matrix
from point import Point
from sphere import Sphere
from patterns.stripe import Stripe


class TestStripe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.white = Color(red=1, green=1, blue=1)
        cls.black = Color(red=0, green=0, blue=0)
        cls.red = Color(red=1, green=0, blue=0)
        cls.green = Color(red=0, green=1, blue=0)

    def test_create_with_default(self):
        s = Stripe()
        self.assertEqual(s.color_a, self.__class__.white)
        self.assertEqual(s.color_b, self.__class__.black)

    def test_create_with_explicit(self):
        s = Stripe(color_a=self.__class__.red, color_b=self.__class__.green)
        self.assertEqual(s.color_a, self.__class__.red)
        self.assertEqual(s.color_b, self.__class__.green)

    def test_color_at_constant_in_y(self):
        s = Stripe()
        self.assertEqual(s.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(s.color_at(position=Point(x=0, y=1, z=0)),
                         self.__class__.white)
        self.assertEqual(s.color_at(position=Point(x=0, y=2, z=0)),
                         self.__class__.white)

    def test_color_at_constant_in_z(self):
        s = Stripe()
        self.assertEqual(s.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(s.color_at(position=Point(x=0, y=0, z=1)),
                         self.__class__.white)
        self.assertEqual(s.color_at(position=Point(x=0, y=0, z=2)),
                         self.__class__.white)

    def test_color_at_alternates_in_x(self):
        s = Stripe()
        self.assertEqual(s.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(s.color_at(position=Point(x=0.9, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(s.color_at(position=Point(x=1, y=0, z=0)),
                         self.__class__.black)
        self.assertEqual(s.color_at(position=Point(x=-0.1, y=0, z=0)),
                         self.__class__.black)
        self.assertEqual(s.color_at(position=Point(x=-1, y=0, z=0)),
                         self.__class__.black)
        self.assertEqual(s.color_at(position=Point(x=-1.1, y=0, z=0)),
                         self.__class__.white)

    def test_color_at_shape_with_object_transform(self):
        s = Sphere(transform=Matrix.scaling_transform(x=2, y=2, z=2))
        p = Stripe(color_a=self.__class__.white, color_b=self.__class__.black)
        c = p.shape_color_at(shape=s, position=Point(x=1.5, y=0, z=0))
        self.assertEqual(c, self.__class__.white)

    def test_color_at_shape_with_pattern_transform(self):
        s = Sphere()
        p = Stripe(color_a=self.__class__.white,
                   color_b=self.__class__.black,
                   transform=Matrix.scaling_transform(x=2, y=2, z=2))
        c = p.shape_color_at(shape=s, position=Point(x=1.5, y=0, z=0))
        self.assertEqual(c, self.__class__.white)

    def test_color_at_shape_with_object_and_pattern_transform(self):
        s = Sphere(transform=Matrix.scaling_transform(x=2, y=2, z=2))
        p = Stripe(color_a=self.__class__.white,
                   color_b=self.__class__.black,
                   transform=Matrix.translation_transform(x=0.5, y=0, z=0))
        c = p.shape_color_at(shape=s, position=Point(x=2.5, y=0, z=0))
        self.assertEqual(c, self.__class__.white)


if __name__ == '__main__':
    unittest.main()
