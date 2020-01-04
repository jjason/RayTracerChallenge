import math
import unittest

from camera import Camera
from color import Color
from lights import PointLight
from matrix import Matrix
from point import Point
from sphere import Sphere
from util import Utilities
from vector import Vector
from world import World


class TestCamera(unittest.TestCase):
    def setUp(self):
        light_source = PointLight(position=Point(x=-10, y=10, z=-10),
                                  intensity=Color(red=1, green=1, blue=1))
        s1 = Sphere()
        s1.material.color = Color(red=0.8, green=1.0, blue=0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2

        s2 = Sphere()
        s2.transform = Matrix.scaling_transform(x=0.5, y=0.5, z=0.5)

        self._default_world = World(objects=[s1, s2], light_source=light_source)

    def test_create(self):
        h = 160
        v = 120
        f = math.pi/2
        c = Camera(horizontal_size=h, vertical_size=v, field_of_view=f)
        self.assertEqual(c.horizontal_size, h)
        self.assertEqual(c.vertical_size, v)
        self.assertEqual(c.field_of_view, math.pi/2)

    def test_pixel_size_horizontal_canvas(self):
        c = Camera(horizontal_size=200,
                   vertical_size=125,
                   field_of_view=math.pi/2)
        self.assertTrue(Utilities.equal(c.pixel_size, 0.01))

    def test_pixel_size_vertical_canvas(self):
        c = Camera(horizontal_size=125,
                   vertical_size=200,
                   field_of_view=math.pi/2)
        self.assertTrue(Utilities.equal(c.pixel_size, 0.01))

    def test_ray_through_center_of_canvas(self):
        c = Camera(horizontal_size=201,
                   vertical_size=101,
                   field_of_view=math.pi/2)
        r = c.ray_for_pixel(x=100, y=50)
        self.assertEqual(r.origin, Point(x=0, y=0, z=0))
        self.assertEqual(r.direction, Vector(x=0, y=0, z=-1))

    def test_ray_through_upper_left_corner_of_canvas(self):
        c = Camera(horizontal_size=201,
                   vertical_size=101,
                   field_of_view=math.pi/2)
        r = c.ray_for_pixel(x=0, y=0)
        self.assertEqual(r.origin, Point(x=0, y=0, z=0))
        self.assertEqual(r.direction, Vector(x=0.66519, y=0.33259, z=-0.66851))

    def test_ray_with_transformed_camera(self):
        c = Camera(horizontal_size=201,
                   vertical_size=101,
                   field_of_view=math.pi/2)
        c.transform = Matrix.rotation_y_transform(radians=math.pi/4) * \
                      Matrix.translation_transform(x=0, y=-2, z=5)
        r = c.ray_for_pixel(x=100, y=50)
        self.assertEqual(r.origin, Point(x=0, y=2, z=-5))
        self.assertEqual(r.direction, Vector(x=math.sqrt(2)/2,
                                             y=0,
                                             z=-math.sqrt(2)/2))

    def test_render(self):
        c = Camera(horizontal_size=11,
                   vertical_size=11,
                   field_of_view=math.pi/2)
        e = Point(x=0, y=0, z=-5)
        t = Point(x=0, y=0, z=0)
        u = Vector(x=0, y=1, z=0)
        c.transform = Matrix.view_transform(eye=e, to=t, up=u)
        i = c.render(self._default_world)
        self.assertEqual(i.get_pixel(x=5, y=5), Color(red=0.38066,
                                                      green=0.47583,
                                                      blue=0.2855))


if __name__ == '__main__':
    unittest.main()
