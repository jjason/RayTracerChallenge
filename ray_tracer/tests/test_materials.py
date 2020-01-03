import math
import unittest

from color import Color
from lights import PointLight
from materials import Material
from point import Point
from util import Utilities
from vector import Vector


class TestMaterial(unittest.TestCase):
    def setUp(self):
        self._material = Material()
        self._position = Point(x=0, y=0, z=0)

    def test_create_default(self):
        self.assertEqual(self._material.color, Color(red=1, green=1, blue=1))
        self.assertTrue(Utilities.equal(self._material.ambient, 0.1))
        self.assertTrue(Utilities.equal(self._material.diffuse, 0.9))
        self.assertTrue(Utilities.equal(self._material.specular, 0.9))
        self.assertTrue(Utilities.equal(self._material.shininess, 200.0))

    def test_set_ambient(self):
        self._material.ambient = 0.0
        self.assertTrue(Utilities.equal(self._material.ambient, 0.0))
        self._material.ambient = 0.5
        self.assertTrue(Utilities.equal(self._material.ambient, 0.5))

    def test_set_ambient_negative(self):
        self._material.ambient = -0.5
        self.assertTrue(Utilities.equal(self._material.ambient, 0.1))

    def test_set_diffuse(self):
        self._material.diffuse = 0.0
        self.assertTrue(Utilities.equal(self._material.diffuse, 0.0))
        self._material.diffuse = 0.5
        self.assertTrue(Utilities.equal(self._material.diffuse, 0.5))

    def test_set_diffuse_negative(self):
        self._material.diffuse = -0.5
        self.assertTrue(Utilities.equal(self._material.diffuse, 0.9))

    def test_set_specular(self):
        self._material.specular = 0.0
        self.assertTrue(Utilities.equal(self._material.specular, 0.0))
        self._material.specular = 0.5
        self.assertTrue(Utilities.equal(self._material.specular, 0.5))

    def test_set_specular_negative(self):
        self._material.specular = -0.5
        self.assertTrue(Utilities.equal(self._material.specular, 0.9))

    def test_set_shininess(self):
        self._material.shininess = 0.0
        self.assertTrue(Utilities.equal(self._material.shininess, 0.0))
        self._material.shininess = 0.5
        self.assertTrue(Utilities.equal(self._material.shininess, 0.5))

    def test_set_shininess_negative(self):
        self._material.shininess = -0.5
        self.assertTrue(Utilities.equal(self._material.shininess, 200.0))

    def test_lighting_eye_and_light_opposite_surface(self):
        #
        #                |
        #                |
        # l    e   <--n--|
        #                |
        #                |
        #
        e = Vector(x=0, y=0, z=-1)
        n = Vector(x=0, y=0, z=-1)
        l = PointLight(position=Point(x=0, y=0, z=-10),
                       intensity=Color(red=1, green=1, blue=1))
        c = self._material.lighting(light=l,
                                    position=self._position,
                                    eye=e,
                                    normal=n)
        self.assertEqual(c, Color(red=1.9, blue=1.9, green=1.9))

    def test_lighting_eye_offset_45_and_light_opposite_surface(self):
        #
        #             e
        #              \ |
        #               \|
        # l        <--n--|
        #                |
        #                |
        #
        e = Vector(x=0, y=math.sqrt(2)/2, z=-math.sqrt(2)/2)
        n = Vector(x=0, y=0, z=-1)
        l = PointLight(position=Point(x=0, y=0, z=-10),
                       intensity=Color(red=1, green=1, blue=1))
        c = self._material.lighting(light=l,
                                    position=self._position,
                                    eye=e,
                                    normal=n)
        self.assertEqual(c, Color(red=1.0, blue=1.0, green=1.0))

    def test_lighting_eye_opposite_and_light_offset_45_surface(self):
        #
        #             l
        #              \ |
        #               \|
        #       e  <--n--|
        #                |
        #                |
        #
        e = Vector(x=0, y=0, z=-1)
        n = Vector(x=0, y=0, z=-1)
        l = PointLight(position=Point(x=0, y=10, z=-10),
                       intensity=Color(red=1, green=1, blue=1))
        c = self._material.lighting(light=l,
                                    position=self._position,
                                    eye=e,
                                    normal=n)
        self.assertEqual(c, Color(red=0.7364, blue=0.7364, green=0.7364))

    def test_lighting_eye_offset_neg_45_and_light_offset_45_surface(self):
        #
        #             l
        #              \ |
        #               \|
        #          <--n--|
        #               /|
        #              / |
        #             e
        #
        e = Vector(x=0, y=-math.sqrt(2)/2, z=-math.sqrt(2)/2)
        n = Vector(x=0, y=0, z=-1)
        l = PointLight(position=Point(x=0, y=10, z=-10),
                       intensity=Color(red=1, green=1, blue=1))
        c = self._material.lighting(light=l,
                                    position=self._position,
                                    eye=e,
                                    normal=n)
        self.assertEqual(c, Color(red=1.6364, blue=1.6364, green=1.6364))

    def test_lighting_eye_opposite_and_light_behind_surface(self):
        #
        #                |
        #                |
        #      e   <--n--|       l
        #                |
        #                |
        #
        e = Vector(x=0, y=0, z=-1)
        n = Vector(x=0, y=0, z=-1)
        l = PointLight(position=Point(x=0, y=0, z=10),
                       intensity=Color(red=1, green=1, blue=1))
        c = self._material.lighting(light=l,
                                    position=self._position,
                                    eye=e,
                                    normal=n)
        self.assertEqual(c, Color(red=0.1, blue=0.1, green=0.1))


if __name__ == '__main__':
    unittest.main()