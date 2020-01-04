from color import Color
from intersections import Computations, Intersections


class World:
    def __init__(self, objects=None, light_source=None):
        self._objects = objects if objects else []
        self._light_source = light_source

    @property
    def objects(self):
        return self._objects

    @property
    def light_source(self):
        return self._light_source

    @light_source.setter
    def light_source(self, value):
        self._light_source = value

    def intersect(self, ray):
        total_intersections = []

        # Walk through all of the objects in the world and find the
        # intersections
        for the_object in self._objects:
            intersections = the_object.intersect(ray=ray)
            for index in range(intersections.count):
                total_intersections.append(intersections[index])

        # Sort the intersections by time
        total_intersections.sort(key=lambda i: i.time)

        return Intersections(*total_intersections)

    def shade_hit(self, computations=Computations()):
        return computations.the_object.material.lighting(light=self._light_source,
                                                         position=computations.position,
                                                         eye=computations.eye,
                                                         normal=computations.normal)

    def color_at(self, ray):
        # Determine the intersections for the ray and the objects in the world
        intersections = self.intersect(ray=ray)

        # If there is not a hit (either all misses or an intersection would
        # be behind the ray), then return black color
        intersection = intersections.hit()
        if not intersection:
            return Color(red=0, green=0, blue=0)

        # Otherwise, prepare the computations for the ray and return the color
        computations = intersection.prepare_computations(ray=ray)
        color = self.shade_hit(computations=computations)

        return color

