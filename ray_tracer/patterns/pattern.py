from color import Color
from matrix import Matrix


class Pattern:
    """
    The base class from which all patterns will derive.  Contains the common
    properties and methods for patterns.
    """
    def __init__(self, color_a=None, color_b=None, transform=None):
        """
        Initialize a newly-created Pattern object.

        :param color_a: The color between x = [0, 1), [2, 3), [4, 5), etc.  If
            not provided, default is white.
        :param color_b: The color between x = [1, 2), [3, 4), [5, 6), etc.  If
            not provided, default is black
        :param transform: The transform to be applied to the pattern.  If None,
            then the identity transform is used.
        """
        self.color_a = color_a
        self.color_b = color_b
        self.transform = transform

    @property
    def color_a(self):
        return self._color_a

    @color_a.setter
    def color_a(self, value):
        self._color_a = value if value else Color(red=1, green=1, blue=1)

    @property
    def color_b(self):
        return self._color_b

    @color_b.setter
    def color_b(self, value):
        self._color_b = value if value else Color(red=0, green=0, blue=0)

    @property
    def transform(self):
        return self._transform

    @transform.setter
    def transform(self, value):
        self._transform = value if value else Matrix.identity()
        self._inverse_transform = self._transform.inverse()

    def color_at(self, position):
        """
        Return the color for the pattern at the position provided.

        :param position: Point, the point for which color is to be determined.
        :return: Color, the color for the position.
        """
        raise NotImplementedError(
                "{} does not implement color_at".format(self.__class__.__name__))

    def shape_color_at(self, shape, position):
        """
        Return the color for the pattern on the shape at the world-space
        position.

        :param shape: Shape, the shape upon which the pattern color will be
            returned.
        :param position: Point, the world-space position on the shape for which
            the pattern color will be returned.
        :return: Color, the color for the pattern on the shape at the position
            provided.
        """
        # First convert the position from world space to object space
        object_position = shape.transform.inverse() * position

        # Then convert the position from object space to pattern space
        pattern_position = self._inverse_transform * object_position

        # Now figure out the color for the patter space position
        return self.color_at(position=pattern_position)
