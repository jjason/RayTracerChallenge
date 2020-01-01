from util import Utilities

class Tuple:
    def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def is_point(self):
        return Utilities.equal(self.w, 1.0)

    def is_vector(self):
        return Utilities.equal(self.w, 0.0)

    def __eq__(self, other):
        return Utilities.equal(self.x, other.x) and \
               Utilities.equal(self.y, other.y) and \
               Utilities.equal(self.z, other.z) and \
               Utilities.equal(self.w, other.w)

    def __add__(self, other):
        # It does not make sense to add two points
        if self.is_point() and other.is_point():
            raise TypeError("Cannot add two points")

        return Tuple(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z,
                     self.w + other.w)

    def __sub__(self, other):
        # It does not make sense to subtract a point from a vector
        if self.is_vector() and other.is_point():
            raise TypeError("Cannot subtract a point from a vector")

        return Tuple(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z,
                     self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, scalar):
        return Tuple(self.x * scalar,
                     self.y * scalar,
                     self.z * scalar,
                     self.w * scalar)

    def __truediv__(self, scalar):
        return Tuple(self.x / scalar,
                     self.y / scalar,
                     self.z / scalar,
                     self.w / scalar)

    def __str__(self):
        return "x={}, y={}, z={}, w={}".format(self.x, self.y, self.z, self.w)