from intersections import Intersection, Intersections
from shape import Shape
from util import Utilities
from vector import Vector


class Plane(Shape):
    """
    Represents an xz plane, i.e., a plane that stretches infinitely in the x and
    z directions and passing through the origin.  To get a different plane,
    assign a transform to it.
    """
    def __init__(self,
                 transform=None,
                 material=None):
        """
        Initialize a Plane object

        :param transform: The transform to be applied to the plane
        :param material: The material for the plane
        """
        super().__init__(transform=transform, material=material)

    def _intersect(self, ray):
        """
        Override base class method to provide plane-specific method for
        computing intersection with ray and plane.

        This method should not be called directly.  Instead, call the public
        intersect method defined in the Shape class.

        :param ray: The ray we use to compute intersection.
        :return: Intersections, the set of Intersection objects representing
            the intersection between the provided ray and this plane.
        """
        # First we need to determine if the ray is parallel (coplanar will also
        # count as parallel as we would be viewing the plane edge-on).  A ray
        # is parallel if the y component is zero (or, really, really close to
        # zero).
        if abs(ray.direction.y) < Utilities.EPSILON:
            return Intersections()

        # Compute the amount of time it takes the ray to go from its origin in
        # the y direction until it gets to y=0.  Simply divide the ray origin's
        # y value by the ray direction's y value and negate
        time = -ray.origin.y / ray.direction.y
        return Intersections(Intersection(time=time, the_object=self))

    def _normal_at(self, position):
        """
        Override base class method to provide plane-specific method for
        computing normal at the point specified.

        This method should not be called directly.  Instead, call the public
        normal_at method defined in the Shape class.

        :param position: The position on the sphere for which the normal is
            to be computed.
        :return: Vector, the normal at the point provided.
        """
        # Because we are implementing an xz plane, all points have the same
        # normal, the vector (0, 1, 0)
        return Vector(x=0, y=1, z=0)
