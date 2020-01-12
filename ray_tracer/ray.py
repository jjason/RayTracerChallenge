from matrix import Matrix
from point import Point
from vector import Vector


class Ray:
    def __init__(self, origin=None, direction=None):
        self.origin = origin
        self.direction = direction

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = Point(x=value.x, y=value.y, z=value.z) \
            if value else Point(x=0, y=0, z=0)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = Vector(x=value.x, y=value.y, z=value.z) \
            if value else Vector(x=0, y=0, z=0)

    def position(self, time=0):
        return self._origin + (self._direction * time)

    def transform(self, transformation=Matrix.identity()):
        return Ray(origin=transformation * self._origin,
                   direction=transformation * self._direction)

    def __eq__(self, other):
        return (self.origin == other.origin) and (self.direction == other.direction)

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "origin: {} direction: {}".format(self._origin, self._direction)