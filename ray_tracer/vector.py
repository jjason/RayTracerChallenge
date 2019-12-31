from math import sqrt
from tuple import Tuple

class Vector(Tuple):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x=x, y=y, z=z, w=0.0)

    def magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    @staticmethod
    def normalize(vector):
        magnitude = vector.magnitude()
        return Vector(vector.x / magnitude,
                      vector.y / magnitude,
                      vector.z / magnitude)

    @staticmethod
    def dot_product(lhs, rhs):
        return lhs.x * rhs.x + \
               lhs.y * rhs.y + \
               lhs.z * rhs.z

    @staticmethod
    def cross_product(lhs, rhs):
        return Vector(lhs.y * rhs.z - lhs.z * rhs.y,
                      lhs.z * rhs.x - lhs.x * rhs.z,
                      lhs.x * rhs.y - lhs.y * rhs.x)
