from tuple import Tuple

class Color(Tuple):
    def __init__(self, red=0.0, green=0.0, blue=0.0):
        super().__init__(x=red, y=green, z=blue, w=0.0)

    """
    RGB properties that forward on to the underlying Tuple x/y/z
    attributes.
    """

    @property
    def red(self):
        return self.x

    @red.setter
    def red(self, value):
        self.x = value

    @property
    def green(self):
        return self.y

    @green.setter
    def green(self, value):
        self.y = value

    @property
    def blue(self):
        return self.z

    @blue.setter
    def blue(self, value):
        self.z = value

    @staticmethod
    def _clamp_color_value(value):
        # We want to take the color values that are supposed to be a float
        # [0.0, 1.0] and convert to an integer value [0, 255].  Take the float
        # value, multiply by 255, add 0.5 (to round properly), and convert to
        # integer.  Then convert values below 0 to 0 and values above 255 to
        # 255.
        return min(max(0, int(value * 255 + 0.5)), 255)

    def __mul__(self, rhs):
        # If we are multiplying by another color, then we are going to compute
        # the Hadamard (or Schur) product, which just multiplies each of the
        # RGB components
        if isinstance(rhs, Color):
            return Color(red=(self.red * rhs.red),
                         green=(self.green * rhs.green),
                         blue=(self.blue * rhs.blue))

        # If we are not multiplying by another color, then fall back to the
        # scalar multiplication provided by the base class
        return super().__mul__(rhs)

    def __str__(self):
        return "{} {} {}".format(self._clamp_color_value(self.red),
                                 self._clamp_color_value(self.green),
                                 self._clamp_color_value(self.blue))
