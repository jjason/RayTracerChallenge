import unittest
import math

from color import Color
from point import Point
from patterns.ring import Ring


class TestRing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.white = Color(red=1, green=1, blue=1)
        cls.black = Color(red=0, green=0, blue=0)

    def test_color_should_not_change_with_y(self):
        r = Ring(color_a=self.__class__.white, color_b=self.__class__.black)
        self.assertEqual(r.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(r.color_at(position=Point(x=0, y=1, z=0)),
                         self.__class__.white)
        self.assertEqual(r.color_at(position=Point(x=0, y=2, z=0)),
                         self.__class__.white)

    def test_color_at_should_extend_in_x_and_y(self):
        r = Ring(color_a=self.__class__.white, color_b=self.__class__.black)
        self.assertEqual(r.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(r.color_at(position=Point(x=1, y=0, z=0)),
                         self.__class__.black)
        self.assertEqual(r.color_at(position=Point(x=0, y=0, z=1)),
                         self.__class__.black)
        self.assertEqual(r.color_at(position=Point(x=math.sqrt(2)/2,
                                                   y=0,
                                                   z=math.sqrt(2)/2)),
                         self.__class__.black)


if __name__ == '__main__':
    unittest.main()
