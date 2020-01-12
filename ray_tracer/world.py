from color import Color
from intersections import Computations, Intersections
from ray import Ray


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
        # Determine if the point is shadowed.  To prevent a point on the object
        # from being shadowed by its own point (because of inaccuracies in
        # floating point arithmetic), use the point that is just sightly over
        # the point to prevent false positives.
        is_shadowed = self.is_shadowed(computations.over_position)

        return computations.the_object.material.lighting(light=self._light_source,
                                                         position=computations.position,
                                                         eye=computations.eye,
                                                         normal=computations.normal,
                                                         in_shadow=is_shadowed)

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

    def is_shadowed(self, position):
        """
        Determine if the point defined by position is in the shadow of an object
        in the world, i.e., the ray from the point to the light source
        intersects an object in the world before reaching the light source.

        :param position: The point to test for being in a shadow

        :return: Boolean, True if the point is in a shadow, False otherwise
        """
        # Create a vector from the point to the light source and determine the
        # distance to light source
        vector = self._light_source.position - position
        distance = vector.magnitude()

        # Normalize the vector and then determine if it intersects any objects
        direction = vector.normalize()
        ray = Ray(origin=position, direction=direction)
        intersections = self.intersect(ray=ray)

        # Get the first hit from the intersections and see if the distance from
        # the point to the first hit is less than the distance from the point to
        # the light source.  Because we ensure that hit returns the first non-
        # negative hit, we don't have to worry about a hit that is behind the
        # light source.  If so, then the point is in the shadow.
        hit = intersections.hit()
        return hit and hit.time < distance
