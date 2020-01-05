import unittest

from color import Color
from intersections import Intersection
from lights import PointLight
from matrix import Matrix
from point import Point
from ray import Ray
from sphere import Sphere
from util import Utilities
from vector import Vector
from world import World


class TestWorld(unittest.TestCase):
    def setUp(self):
        self._light_source = PointLight(position=Point(x=-10, y=10, z=-10),
                                        intensity=Color(red=1, green=1, blue=1))
        self._s1 = Sphere()
        self._s1.material.color = Color(red=0.8, green=1.0, blue=0.6)
        self._s1.material.diffuse = 0.7
        self._s1.material.specular = 0.2

        self._s2 = Sphere()
        self._s2.transform = Matrix.scaling_transform(x=0.5, y=0.5, z=0.5)

        self._default_world = World(objects=[self._s1, self._s2],
                                    light_source=self._light_source)

    def test_create_empty_world(self):
        w = World()
        self.assertEqual(len(w.objects), 0)
        self.assertIsNone(w.light_source)

    def test_create_default_world(self):
        self.assertEqual(self._light_source, self._default_world.light_source)
        self.assertIn(self._s1, self._default_world.objects)
        self.assertIn(self._s2, self._default_world.objects)

    def test_intersect_ray(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        i = self._default_world.intersect(ray=r)
        self.assertEqual(i.count, 4)
        self.assertTrue(Utilities.equal(i[0].time, 4))
        self.assertTrue(Utilities.equal(i[1].time, 4.5))
        self.assertTrue(Utilities.equal(i[2].time, 5.5))
        self.assertTrue(Utilities.equal(i[3].time, 6))

    def test_shade_hit_outside(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        s = self._default_world.objects[0]
        i = Intersection(time=4, the_object=s)
        c = i.prepare_computations(ray=r)
        co = self._default_world.shade_hit(c)
        self.assertEqual(co, Color(red=0.38066, green=0.47583, blue=0.2855))

    def test_shade_hit_inside(self):
        self._default_world.light_source = PointLight(position=Point(x=0,
                                                                     y=0.25,
                                                                     z=0),
                                                      intensity=Color(red=1,
                                                                      green=1,
                                                                      blue=1))
        r = Ray(origin=Point(x=0, y=0, z=0), direction=Vector(x=0, y=0, z=1))
        s = self._default_world.objects[1]
        i = Intersection(time=0.5, the_object=s)
        c = i.prepare_computations(ray=r)
        co = self._default_world.shade_hit(c)
        self.assertEqual(co, Color(red=0.90498, green=0.90498, blue=0.90498))

    def test_color_at_when_ray_misses(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=1, z=0))
        c = self._default_world.color_at(ray=r)
        self.assertEqual(c, Color(red=0, green=0, blue=0))

    def test_color_at_when_ray_hits(self):
        r = Ray(origin=Point(x=0, y=0, z=-5), direction=Vector(x=0, y=0, z=1))
        c = self._default_world.color_at(ray=r)
        self.assertEqual(c, Color(red=0.38066, green=0.47583, blue=0.2855))

    def test_color_at_intersection_behind_ray(self):
        o = self._default_world.objects[0]
        o.material.ambient = 1
        i = self._default_world.objects[1]
        i.material.ambient = 1
        r = Ray(origin=Point(x=0, y=0, z=0.75), direction=Vector(x=0, y=0, z=-1))
        c = self._default_world.color_at(ray=r)
        self.assertEqual(c, i.material.color)


if __name__ == '__main__':
    unittest.main()
