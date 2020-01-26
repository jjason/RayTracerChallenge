import unittest

from color import Color
from point import Point
from patterns.gradient import Gradient


class TestGradient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.white = Color(red=1, green=1, blue=1)
        cls.black = Color(red=0, green=0, blue=0)

    def test_color_at_interpolates_between_colors(self):
        g = Gradient(color_a=self.__class__.white, color_b=self.__class__.black)
        self.assertEqual(g.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(g.color_at(position=Point(x=0.25, y=0, z=0)),
                         Color(red=0.75, green=0.75, blue=0.75))
        self.assertEqual(g.color_at(position=Point(x=0.5, y=0, z=0)),
                         Color(red=0.5, green=0.5, blue=0.5))
        self.assertEqual(g.color_at(position=Point(x=0.75, y=0, z=0)),
                         Color(red=0.25, green=0.25, blue=0.25))


if __name__ == '__main__':
    unittest.main()
