from color import Color
from point import Point


class PointLight:
    def __init__(self,
                 position=Point(x=0, y=0, z=0),
                 intensity=Color(red=1, green=1, blue=1)):
        self._position = Point(x=position.x, y=position.y, z=position.z)
        self._intensity = Color(red=intensity.red,
                                green=intensity.green,
                                blue=intensity.blue)

    @property
    def position(self):
        return self._position

    @property
    def intensity(self):
        return self._intensity

