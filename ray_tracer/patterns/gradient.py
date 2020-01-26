import math

from patterns.pattern import Pattern


class Gradient(Pattern):
    """
    The gradient pattern.  A gradient pattern has two colors and blends between
    them as the point moves in the x direction between coordinates.  For a point
    with an x coordinate px, floor(px) is color_a and floor(px) + 1 is color_b.
    To determine the color of px, do a linear interpolation between color_a and
    color_b between floor(px) and px.  i.e.,

    color @ px = color_a + (color_b - color_a) * (px - floor(px))

    The color is independent of y and z coordinates.
    """
    def __init__(self,
                 color_a=None,
                 color_b=None,
                 transform=None):
        """
        Initialize the gradient pattern object.

        :param color_a: The color at floor(x coordinate).  If not provided,
            default is white.
        :param color_b: The color at floor(x coordinate) + 1.  If not provided,
            default is black
        :param transform: The transform to be applied to the pattern.  If None,
            then the identity transform is used.
        """
        super().__init__(color_a=color_a, color_b=color_b, transform=transform)

    def color_at(self, position):
        """
        Return the interpolated color for the position provided.  The color is
        determined as described above.

        :param position: The point for which color is to be determined.
        :return: Color, the color for the point.
        """
        distance = self.color_b - self.color_a
        fraction = position.x - math.floor(position.x)

        return self.color_a + (distance * fraction)
