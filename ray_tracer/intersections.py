from point import Point
from ray import Ray
from util import Utilities
from vector import Vector


class Computations:
    def __init__(self,
                 time=0.0,
                 shape=None,
                 position=None,
                 eye=None,
                 normal=None):
        self.time = time
        self.shape = shape
        self.position = position
        self.eye = eye
        self.normal = normal
        self.inside = False
        self.over_position = 0

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        self._shape = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value if value else Point()

    @property
    def eye(self):
        return self._eye

    @eye.setter
    def eye(self, value):
        self._eye = value if value else Vector()

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, value):
        self._normal = value if value else Vector()

    @property
    def inside(self):
        return self._inside

    @inside.setter
    def inside(self, value):
        self._inside = value

    @property
    def over_position(self):
        return self._over_position

    @over_position.setter
    def over_position(self, value):
        self._over_position = value


class Intersection:
    def __init__(self, time=0.0, shape=None):
        self.time = time
        self.shape = shape

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        self._shape = value

    def prepare_computations(self, ray=Ray()):
        computations = Computations()

        # Copy simple values from intersection
        computations.time = self.time
        computations.shape = self.shape

        # Precompute useful values:
        # - the position on the ray where intersection occurs
        # - the vector to the eye (i.e., the reverse of the array)
        # - the normal at the point of intersection
        computations.position = ray.position(self.time)
        computations.eye = -ray.direction
        computations.normal = self.shape.normal_at(position=computations.position)

        # If the normal vector points away from the eye vector (i.e., the dot
        # product is less than zero), then the hit was inside the object.  We
        # need to set the inside flag appropriately and negate the normal
        # vector to point into the object.
        if computations.normal.dot_product(computations.eye) < 0:
            computations.inside = True
            computations.normal = -computations.normal

        # To prevent an object from casting a shadow over itself (because of
        # inaccuracies in floating point arithmetic), adjust the point just
        # slightly in the direction of the normal.  It is this point that will
        # actually be used when determining if the point is in a shadow to keep
        # from accidentally shadowing a point from the object it belongs to.
        computations.over_position = computations.position + \
                                     computations.normal * \
                                     Utilities.EPSILON

        return computations


class Intersections:
    def __init__(self, *intersections):
        self._intersections = [intersection for intersection in intersections]

    @property
    def count(self):
        return len(self._intersections)

    def __getitem__(self, item):
        return self._intersections[item]

    def hit(self):
        hit = None
        for intersection in self._intersections:
            if intersection.time >= 0 and (hit is None or hit.time > intersection.time):
                hit = intersection

        return hit
