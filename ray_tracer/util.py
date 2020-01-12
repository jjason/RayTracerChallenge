class Utilities:
    EPSILON = 0.00001

    @staticmethod
    def equal(a, b):
        return abs(a - b) < Utilities.EPSILON
