from color import Color
from point import Point


class PointLight:
    def __init__(self,
                 position=None,
                 intensity=None):
        self.position = position
        self.intensity = intensity

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = Point(x=value.x, y=value.y, z=value.z) \
            if value else Point(x=0, y=0, z=0)

    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, value):
        self._intensity = Color(red=value.red,
                                green=value.green,
                                blue=value.blue) \
            if value else Color(red=1, green=1, blue=1)

    def __eq__(self, other):
        return self.position == other.position and \
               self.intensity == other.intensity

    def __ne__(self, other):
        return not self == other
