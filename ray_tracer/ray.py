from matrix import Matrix
from point import Point
from vector import Vector


class Ray:
    def __init__(self, origin=Point(), direction=Vector()):
        self._origin = Point(x=origin.x, y=origin.y, z=origin.z)
        self._direction = Vector(x=direction.x, y=direction.y, z=direction.z)

    @property
    def origin(self):
        return self._origin

    @property
    def direction(self):
        return self._direction

    def position(self, time=0):
        return self._origin + (self._direction * time)

    def transform(self, transformation=Matrix.identity()):
        return Ray(origin=transformation * self._origin,
                   direction=transformation * self._direction)

    def __str__(self):
        return "origin: {} direction: {}".format(self._origin, self._direction)