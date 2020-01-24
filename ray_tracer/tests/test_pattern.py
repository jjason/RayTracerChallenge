import unittest
from unittest import mock

from color import Color
from matrix import Matrix
from patterns.pattern import Pattern
from point import Point
from sphere import Sphere


class TestPattern(unittest.TestCase):
    def setUp(self):
        self._shape = Sphere()
        self._pattern = Pattern()

    def test_color_at_raises_exception(self):
        with self.assertRaises(NotImplementedError):
            self._pattern.color_at(position=Point(x=0, y=0, z=0))

    def test_default_transformation(self):
        p = Pattern()
        self.assertEqual(p.transform, Matrix.identity())

    def test_set_transformation(self):
        p = Pattern(transform=Matrix.translation_transform(x=1, y=2, z=3))
        self.assertEqual(p.transform,
                         Matrix.translation_transform(x=1, y=2, z=3))

    def test_shape_color_at_with_object_transform(self):
        self._shape.transform = Matrix.scaling_transform(x=2, y=2, z=2)

        # Replace the base Pattern class color_at method that is to be
        # overridden by derived classes with a MagicMock so we can see if the
        # base class calls the color_at method after the position has been
        # transformed to pattern space.
        self._pattern.color_at = mock.MagicMock(return_value=Color(red=1,
                                                                   green=1,
                                                                   blue=1))
        self._pattern.shape_color_at(shape=self._shape,
                                     position=Point(x=2, y=3, z=4))

        xp = Point(x=1, y=1.5, z=2)
        self._pattern.color_at.assert_called_with(position=xp)

    def test_shape_color_at_with_pattern_transform(self):
        self._pattern.transform = Matrix.scaling_transform(x=2, y=2, z=2)

        # Replace the base Pattern class color_at method that is to be
        # overridden by derived classes with a MagicMock so we can see if the
        # base class calls the color_at method after the position has been
        # transformed to pattern space.
        self._pattern.color_at = mock.MagicMock(return_value=Color(red=1,
                                                                   green=1,
                                                                   blue=1))
        self._pattern.shape_color_at(shape=self._shape,
                                     position=Point(x=2, y=3, z=4))

        xp = Point(x=1, y=1.5, z=2)
        self._pattern.color_at.assert_called_with(position=xp)

    def test_shape_color_at_with_object_and_pattern_transform(self):
        self._shape.transform = Matrix.scaling_transform(x=2, y=2, z=2)
        self._pattern.transform = Matrix.translation_transform(x=0.5,
                                                               y=1,
                                                               z=1.5)

        # Replace the base Pattern class color_at method that is to be
        # overridden by derived classes with a MagicMock so we can see if the
        # base class calls the color_at method after the position has been
        # transformed to pattern space.
        self._pattern.color_at = mock.MagicMock(return_value=Color(red=1,
                                                                   green=1,
                                                                   blue=1))
        self._pattern.shape_color_at(shape=self._shape,
                                     position=Point(x=2.5, y=3, z=3.5))

        xp = Point(x=0.75, y=0.5, z=0.25)
        self._pattern.color_at.assert_called_with(position=xp)


if __name__ == '__main__':
    unittest.main()
