from color import Color
from point import Point


class PointLight:
    def __init__(self,
                 position=None,
                 intensity=None):
        self._position = Point(x=position.x, y=position.y, z=position.z) \
            if position else Point(x=0, y=0, z=0)
        self._intensity = Color(red=intensity.red,
                                green=intensity.green,
                                blue=intensity.blue) \
            if intensity else Color(red=1, green=1, blue=1)

    @property
    def position(self):
        return self._position

    @property
    def intensity(self):
        return self._intensity

    def __eq__(self, other):
        return self._position == other._position and \
               self._intensity == other._intensity
