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
    def blue(self):
        return self.y

    @blue.setter
    def blue(self, value):
        self.y = value

    @property
    def green(self):
        return self.z

    @green.setter
    def green(self, value):
        self.z = value

    def __mul__(self, rhs):
        # If we are multiplying by another color, then we are going to compute
        # the Hadamard (or Schur) product, which just multiplies each of the
        # RGB components
        if isinstance(rhs, Color):
            return Color(self.red * rhs.red,
                         self.blue * rhs.blue,
                         self.green * rhs.green)

        # If we are not multiplying by another color, then fall back to the
        # scalar multiplication provided by the base class
        return super().__mul__(rhs)
