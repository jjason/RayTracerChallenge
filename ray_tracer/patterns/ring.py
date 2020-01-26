import math

from patterns.pattern import Pattern


class Ring(Pattern):
    """
    The ring pattern.  A ring pattern has two colors and changes based upon
    the x and z coordinates of the point.  The color is determined based upon
    the distance of the point from the point (x=0, y=?, z=0), i.e., circles
    in the xz plane.

                     +- color_a if floor(distance to xz) mod 2 == 0
    color @ point => |
                     +- color_b otherwise

    The color is independent of the y coordinate.
    """
    def __init__(self,
                 color_a=None,
                 color_b=None,
                 transform=None):
        """
        Initialize the stripe pattern object.

        :param color_a: The color between xz distances = [0, 1), [2, 3), [4, 5),
            etc.  If not provided, default is white.
        :param color_b: The color between xz distances = [1, 2), [3, 4), [5, 6),
            etc.  If not provided, default is black
        :param transform: The transform to be applied to the pattern.  If None,
            then the identity transform is used.
        """
        super().__init__(color_a=color_a, color_b=color_b, transform=transform)

    def color_at(self, position):
        """
        Return the color (a or b) for the position provided.  The color is
        determined as described above.

        :param position: The point for which color is to be determined.
        :return: Color, the color for the point.
        """
        distance = math.sqrt(position.x ** 2 + position.z ** 2)

        return self.color_a if math.floor(distance) % 2 == 0 else self.color_b
