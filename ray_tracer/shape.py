from materials import Material
from matrix import Matrix
from point import Point
from ray import Ray


class Shape:
    """
    A base class that is used to define a generic shape and the common data
    and operations that all shapes share.
    """
    def __init__(self,
                 transform=None,
                 material=None):
        """
        Initialize a newly-created Shape object.

        :param transform: The transform to be applied to the shape.  If None,
            then the identity transform is used.
        :param material: The material for the shape.  If None, the default
            material is used.
        """
        self.transform = transform
        self.material = material

    @property
    def transform(self):
        return self._transform

    @transform.setter
    def transform(self, value):
        self._transform = value if value else Matrix.identity()
        self._inverse_transform = self._transform.inverse()
        self._inverse_transform_transpose = self._inverse_transform.transpose()

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value if value else Material()

    def _intersect(self, ray):
        """
        Derived classes must override this method.

        When the public intersect method is called, the base class will invoke
        this method with the ray as defined in object space and the derived
        class then performs its shape-specific intersect algorithm.

        :param ray: The ray in object space that is used to perform test of
            intersection with this shape.
        :return: Intersections, an object that contains the Intersection objects
            representing where the ray intersects the shape
        """
        raise NotImplementedError(
            "{} does not implement _intersect method".format(self.__class__.__name__))

    def _normal_at(self, position):
        """
        Derived classes must override this method.

        When the public normal_at method is called, the base class will invoke
        this method with the point in object space and the derived class then
        perform its shape-specific algorithm for computing the normal at the
        point.

        :param position: The point in object space that is used to compute the
            normal for this shape.
        :return: Vector, the object space normal at the point provided
        """
        raise NotImplementedError(
            "{} does not implement _normal_at method".format(self.__class__.__name__))

    def intersect(self, ray=Ray()):
        """
        Given a ray, return the set of intersections with the shape.

        :param ray: The ray for which to test for intersections with this
            transformed shape.
        :return: Intersections, an object that contains the Intersection objects
            representing where the ray intersects the shape
        """
        # Transform the ray to object space and then let the derived class
        # perform its specific intersect algorithm.
        object_space_ray = ray.transform(self.transform.inverse())
        return self._intersect(ray=object_space_ray)

    def normal_at(self, position=Point()):
        """
        Given a point on the shape return the normal (i.e., the normalized
        vector pointing perpendicular from the shape) at that point.

        :param position: The point on the shape where normal is to be computed.
        :return: Vector, the normal at the point provided.
        """
        # Transform the point to object space and then let the derived class
        # perform its specific algorithm for computing the normal.
        object_normal = self._normal_at(position=self._inverse_transform * position)

        # Convert the object normal to a world normal
        world_normal = self._inverse_transform_transpose * object_normal
        world_normal.w = 0

        return world_normal.normalize()
