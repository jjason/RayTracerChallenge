class Intersection:
    def __init__(self, time=0.0, object=None):
        self._time = time
        self._object = object

    @property
    def time(self):
        return self._time

    @property
    def object(self):
        return self._object


class Intersections:
    def __init__(self, *intersections):
        self._intersections = [intersection for intersection in intersections]

    @property
    def count(self):
        return len(self._intersections)

    def __getitem__(self, item):
        return self._intersections[item]

    def hit(self):
        hit = None
        for intersection in self._intersections:
            if intersection.time >= 0 and (hit is None or hit.time > intersection.time):
                hit = intersection

        return hit
