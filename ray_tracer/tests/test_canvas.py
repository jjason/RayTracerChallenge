import unittest

from canvas import Canvas
from color import Color

class TestCanvas(unittest.TestCase):
    def test_create(self):
        c = Canvas(width=10, height=20)
        self.assertEqual(c.width, 10)
        self.assertEqual(c.height, 20)
        black = Color(red=0, green=0, blue=0)
        self.assertTrue(all([c.get_pixel(x=x, y=y) == black
                             for x in range(c.width)
                             for y in range(c.height)]))

    def test_get_invalid_x(self):
        c = Canvas(width=10, height=20)
        with self.assertRaises(ValueError):
            c.get_pixel(x=10, y=0)
        with self.assertRaises(ValueError):
            c.get_pixel(x=-1, y=0)

    def test_get_invalid_y(self):
        c = Canvas(width=10, height=20)
        with self.assertRaises(ValueError):
            c.get_pixel(x=0, y=20)
        with self.assertRaises(ValueError):
            c.get_pixel(x=0, y=-1)

    def test_set_invalid_x(self):
        c = Canvas(width=10, height=20)
        red = Color(red=1, green=0, blue=0)
        with self.assertRaises(ValueError):
            c.set_pixel(x=10, y=0, color=red)
        with self.assertRaises(ValueError):
            c.set_pixel(x=-1, y=0, color=red)

    def test_set_invalid_y(self):
        c = Canvas(width=10, height=20)
        red = Color(red=1, green=0, blue=0)
        with self.assertRaises(ValueError):
            c.set_pixel(x=0, y=20, color=red)
        with self.assertRaises(ValueError):
            c.set_pixel(x=0, y=-1, color=red)

    def test_set_pixel(self):
        c = Canvas(width=10, height=20)
        red = Color(red=1, green=0, blue=0)
        c.set_pixel(x=3, y=2, color=red)
        self.assertEqual(c.get_pixel(x=3, y=2), red)

    def test_to_ppm_header(self):
        c = Canvas(width=5, height=3)
        self.assertTrue(c.to_ppm().startswith("P3\n5 3\n255\n"))

    def test_to_ppm(self):
        c = Canvas(width=5, height=3)
        c.set_pixel(x=0, y=0, color=Color(red=1.5, green=0, blue=0))
        c.set_pixel(x=2, y=1, color=Color(red=0, green=0.5, blue=0))
        c.set_pixel(x=4, y=2, color=Color(red=-0.5, green=0, blue=1))
        self.assertTrue(c.to_ppm().endswith(
            "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n"
            "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n"
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n"
        ))

    def test_to_ppm_70_column_limit(self):
        c = Canvas(width=10, height=2)
        [c.set_pixel(x=x, y=y, color=Color(red=1, green=0.8, blue=0.6))
         for x in range(c.width)
         for y in range(c.height)]
        self.assertTrue(c.to_ppm().endswith(
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n"
            "153 255 204 153 255 204 153 255 204 153 255 204 153\n"
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n"
            "153 255 204 153 255 204 153 255 204 153 255 204 153\n"
        ))

    def test_to_ppm_ends_with_newline(self):
        c = Canvas(width=5, height=3)
        self.assertTrue(c.to_ppm().endswith("\n"))

if __name__ == '__main__':
    unittest.main()
