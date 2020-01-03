import math

from intersections import Intersection, Intersections
from materials import Material
from matrix import Matrix
from point import Point
from ray import Ray


class Sphere:
    def __init__(self,
                 center=Point(),
                 radius=1.0,
                 transform=Matrix.identity(),
                 material=Material()):
        self._center = Point(x=center.x, y=center.y, z=center.z)
        self._radius = radius
        self._transform = transform
        self._material = material

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    @property
    def transform(self):
        return self._transform

    @transform.setter
    def transform(self, value):
        self._transform = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    def intersect(self, ray=Ray()):
        # Apply any transform to the ray before we find intersection of the
        # ray with this sphere
        ray = ray.transform(transformation=self._transform.inverse())

        # To understand how to compute the intersection of a ray with this
        # sphere, it might be helpful to read this lesson,
        # https://tinyurl.com/tuhcnx7, on the Analytical
        # Solution for Ray-Sphere Intersection.  This Wikipedia page is also
        # helpful for understanding solving the problem for a sphere that is
        # not at the center: https://tinyurl.com/u57fouv
        #
        # TL;DR
        #
        # By taking the equation of a sphere with radius, r, and center, c, any
        # point, p, on the sphere satisfies the equation:
        #
        #        2    2
        # (p - c)  = r
        #
        # The equation of any point on the ray with origin O and direction D:
        #
        # p = O + tD
        #
        # you can substitute the equation for a point on the ray into the
        # equation for the sphere to get:
        #
        #             2    2
        # |O + Dt - c|  = r
        #
        #             2    2
        # |O + Dt - c|  - r  = 0
        #
        #               2    2
        # |(O - c) + Dt|  - r  = 0
        #
        #        2                 2 2    2
        # (O - c)  + 2D(O - c)t + D t  - r  = 0
        #
        # and finally get to a quadratic in the form f(x) = ax^2 + bx + c
        #
        #  2 2                       2    2
        # D t  + 2D(O - c)t + (O - c)  - r = 0
        #
        #      2
        # a = D
        #
        # b = 2 * D * (O - c)
        #
        #            2    2                        2
        # c = (O - c)  - r  = (O - c) * (O - c) - r
        #
        # Note: (O - c) is the ray from the center of the sphere to the origin
        # of the ray.  When the sphere is centered on the origin, the c
        # component disappears.
        #
        # From there we can use our favorite, the quadratic formula,
        #
        #              2
        # -b +/- sqrt(b - 4ac)
        # --------------------
        #        2a
        #
        # and more specifically the discriminant d = (b  - 4ac) to determine how
        # many solutions there are:
        #
        # d < 0 - no solutions
        # d = 0 - 1 solution
        # d > 0 - 2 solutions
        #
        # and then the solution(s) if any exist.
        #
        # Phew.  That is a lot of explaining, but I wanted to make sure that I
        # understood what the code in the book was doing.

        # Create a vector from the center of this sphere to the origin of the
        # ray
        sphere_to_ray = ray.origin - self._center

        # Compute the a, b, and c coefficients for the quadratic equation
        # described above:
        a = ray.direction.dot_product(ray.direction)
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self._radius**2

        # Now compute the discriminant to determine if we even have solutions.
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return Intersections()

        i1 = Intersection(time=(-b - math.sqrt(discriminant)) / (2 * a), object=self)
        i2 = Intersection(time=(-b + math.sqrt(discriminant)) / (2 * a), object=self)

        return Intersections(i1, i2)

    def normal_at(self, position=Point()):
        inverse_transform = self._transform.inverse()

        object_point = inverse_transform * position
        object_normal = object_point - Point(x=0, y=0, z=0)

        normal = inverse_transform.transpose() * object_normal
        normal.w = 0.0

        return normal.normalize()
