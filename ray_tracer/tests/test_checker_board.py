import unittest

from color import Color
from point import Point
from patterns.checker_board import CheckerBoard


class TestCheckerBoard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.white = Color(red=1, green=1, blue=1)
        cls.black = Color(red=0, green=0, blue=0)

    def test_color_should_repeat_in_x(self):
        c = CheckerBoard(color_a=self.__class__.white,
                         color_b=self.__class__.black)
        self.assertEqual(c.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(c.color_at(position=Point(x=0.99, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(c.color_at(position=Point(x=1.01, y=0, z=0)),
                         self.__class__.black)

    def test_color_should_repeat_in_y(self):
        c = CheckerBoard(color_a=self.__class__.white,
                         color_b=self.__class__.black)
        self.assertEqual(c.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(c.color_at(position=Point(x=0, y=0.99, z=0)),
                         self.__class__.white)
        self.assertEqual(c.color_at(position=Point(x=0, y=1.01, z=0)),
                         self.__class__.black)

    def test_color_should_repeat_in_z(self):
        c = CheckerBoard(color_a=self.__class__.white,
                         color_b=self.__class__.black)
        self.assertEqual(c.color_at(position=Point(x=0, y=0, z=0)),
                         self.__class__.white)
        self.assertEqual(c.color_at(position=Point(x=0, y=0, z=0.99)),
                         self.__class__.white)
        self.assertEqual(c.color_at(position=Point(x=0, y=0, z=1.01)),
                         self.__class__.black)


if __name__ == '__main__':
    unittest.main()
