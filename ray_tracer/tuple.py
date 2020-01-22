import math

from util import Utilities


class Tuple:
    def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)
        self._w = float(w)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value

    def is_point(self):
        return Utilities.equal(self._w, 1.0)

    def is_vector(self):
        return Utilities.equal(self._w, 0.0)

    def __eq__(self, other):
        return Utilities.equal(self._x, other.x) and \
               Utilities.equal(self._y, other.y) and \
               Utilities.equal(self._z, other.z) and \
               Utilities.equal(self._w, other.w)

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        # It does not make sense to add two points
        if self.is_point() and other.is_point():
            raise TypeError("Cannot add two points")

        return Tuple(self._x + other.x,
                     self._y + other.y,
                     self._z + other.z,
                     self._w + other.w)

    def __sub__(self, other):
        # It does not make sense to subtract a point from a vector
        if self.is_vector() and other.is_point():
            raise TypeError("Cannot subtract a point from a vector")

        return Tuple(self._x - other.x,
                     self._y - other.y,
                     self._z - other.z,
                     self._w - other.w)

    def __neg__(self):
        return Tuple(-self._x, -self._y, -self._z, -self._w)

    def __mul__(self, scalar):
        return Tuple(self._x * scalar,
                     self._y * scalar,
                     self._z * scalar,
                     self._w * scalar)

    def __truediv__(self, scalar):
        return Tuple(self._x / scalar,
                     self._y / scalar,
                     self._z / scalar,
                     self._w / scalar)

    def __str__(self):
        return "x={}, y={}, z={}, w={}".format(self._x, self._y, self._z, self._w)

    def magnitude(self):
        if not self.is_vector():
            raise NotImplementedError("Only vectors have magnitude")

        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        if not self.is_vector():
            raise NotImplementedError("Only vectors can be normalized")

        magnitude = self.magnitude()
        return Tuple(x=self.x/magnitude,
                     y=self.y/magnitude,
                     z=self.z/magnitude,
                     w=0.0)

    def dot_product(self, rhs):
        if not self.is_vector() or not rhs.is_vector():
            raise NotImplementedError("Dot product requires two vectors")
        return (self._x * rhs._x) + (self._y * rhs._y) + (self._z * rhs._z)

    def cross_product(self, rhs):
        if not self.is_vector() or not rhs.is_vector():
            raise NotImplementedError("Cross product requires two vectors")
        return Tuple(x=self._y * rhs._z - self._z * rhs._y,
                     y=self._z * rhs._x - self._x * rhs._z,
                     z=self._x * rhs._y - self._y * rhs._x,
                     w=0.0)

    def reflect(self, normal):
        if not self.is_vector():
            raise NotImplementedError("Only vectors can be reflected")

        return self - normal * 2 * self.dot_product(normal)
