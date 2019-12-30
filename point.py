from tuple import Tuple

class Point(Tuple):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x=x, y=y, z=z, w=1.0)
