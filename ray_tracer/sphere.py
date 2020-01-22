import math

from intersections import Intersection, Intersections
from point import Point
from shape import Shape


class Sphere(Shape):
    def __init__(self,
                 center=Point(),
                 radius=1.0,
                 transform=None,
                 material=None):
        super().__init__(transform=transform, material=material)
        self.center = center
        self.radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        self._center = Point(x=value.x, y=value.y, z=value.z) \
            if value else Point(x=0, y=0, z=0)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def _intersect(self, ray):
        """
        Override base class method to provide sphere-specific method for
        computing intersection with ray and sphere.

        This method should not be called directly.  Instead, call the public
        intersect method defined in the Shape class.

        :param ray: The ray we use to compute intersections.
        :return: Intersections, the set of Intersection objects representing
            the intersections between the provided ray and this sphere.
        """
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

        i1 = Intersection(time=(-b - math.sqrt(discriminant)) / (2 * a),
                          the_object=self)
        i2 = Intersection(time=(-b + math.sqrt(discriminant)) / (2 * a),
                          the_object=self)

        return Intersections(i1, i2)

    def _normal_at(self, position):
        """
        Override base class method to provide sphere-specific method for
        computing normal at the point specified.

        This method should not be called directly.  Instead, call the public
        normal_at method defined in the Shape class.

        :param position: The position on the sphere for which the normal is
            to be computed.
        :return: Vector, the normal at the point provided.
        """
        return position - Point(x=0, y=0, z=0)
