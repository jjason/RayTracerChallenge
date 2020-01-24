import math

from patterns.pattern import Pattern


class CheckerBoard(Pattern):
    """
    The checker board pattern.  A checker board pattern has two colors and
    changes in all three dimensions such that no two adjacent cubes are the
    same color.  The color is determined by:

                     +- color_a if (|px| + |py| + |pz|) mod 2 == 0
    color @ point => |
                     +- color_b otherwise.
    """
    def __init__(self,
                 color_a=None,
                 color_b=None,
                 transform=None):
        """
        Initialize the stripe pattern object.

        :param color_a: The color for the cubes with anchor point having zero
            or two coordinates with odd values - (0, 0, 0), (1, 1, 0), etc.
            If not provided, default is white.
        :param color_b: The color for the cubes with anchor point having zero
            or two coordinates with even values - (1, 1, 1), (1, 0, 0), etc.
            If not provided, default is black
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
        return self.color_a if (math.floor(position.x) +
                                math.floor(position.y) +
                                math.floor(position.z)) % 2 == 0 else \
               self.color_b
