import unittest

from color import Color
from lights import PointLight
from point import Point


class TestPointLight(unittest.TestCase):
    def test_create(self):
        p = Point(x=0, y=0, z=0)
        i = Color(red=1, green=1, blue=1)
        l = PointLight(position=p, intensity=i)
        self.assertEqual(p, l.position)
        self.assertEqual(i, l.intensity)


if __name__ == '__main__':
    unittest.main()
