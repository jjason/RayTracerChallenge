from util import Utilities


class Color():
    def __init__(self, red=0.0, green=0.0, blue=0.0):
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, value):
        self._green = value

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, value):
        self._blue = value

    @staticmethod
    def _clamp_color_value(value):
        # We want to take the color values that are supposed to be a float
        # [0.0, 1.0] and convert to an integer value [0, 255].  Take the float
        # value, multiply by 255, add 0.5 (to round properly), and convert to
        # integer.  Then convert values below 0 to 0 and values above 255 to
        # 255.
        return min(max(0, int(value * 255 + 0.5)), 255)

    def __eq__(self, other):
        return Utilities.equal(self._red, other._red) and \
               Utilities.equal(self._green, other._green) and \
               Utilities.equal(self._blue, other._blue)

    def __mul__(self, rhs):
        # If we are multiplying by another color, then we are going to compute
        # the Hadamard (or Schur) product, which just multiplies each of the
        # RGB components
        if isinstance(rhs, Color):
            return Color(red=(self._red * rhs._red),
                         green=(self._green * rhs._green),
                         blue=(self._blue * rhs._blue))

        # If we are not multiplying by another color, then fall back on scalar
        # multiplication of individual color components
        return Color(red=self._red * rhs,
                     green=self._green * rhs,
                     blue=self._blue * rhs)

    def __add__(self, rhs):
        return Color(red=self._red + rhs._red,
                     green=self._green + rhs._green,
                     blue=self._blue + rhs._blue)

    def __sub__(self, rhs):
        return Color(red=self._red - rhs._red,
                     green=self._green - rhs._green,
                     blue=self._blue - rhs._blue)

    def __str__(self):
        return "{} {} {}".format(self._clamp_color_value(self._red),
                                 self._clamp_color_value(self._green),
                                 self._clamp_color_value(self._blue))
