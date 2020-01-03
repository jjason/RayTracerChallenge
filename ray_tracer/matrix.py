import copy
import math

from tuple import Tuple
from util import Utilities


class Matrix:
    def __init__(self, rows=4, columns=4, values=None):
        if values:
            if len(values) < rows * columns:
                raise ValueError("Matrix needs {} values".format(rows * columns))

            self._values = copy.deepcopy(values)
        else:
            self._values = [0.0 for _ in range(rows * columns)]

        self._rows = rows
        self._columns = columns

    @staticmethod
    def identity(dimensions=4):
        matrix = Matrix(rows=dimensions, columns=dimensions)

        # Set the matrix diagonal values to 1.0
        [matrix.set_item(row=dimension, column=dimension, value=1.0)
         for dimension in range(dimensions)]

        return matrix

    @staticmethod
    def translation_transform(x=0, y=0, z=0):
        # Translation matrix is:
        # | 1 0 0 x |
        # | 0 1 0 y |
        # | 0 0 1 z |
        # | 0 0 0 1 |

        m = Matrix.identity(dimensions=4)
        m.set_item(row=0, column=3, value=x)
        m.set_item(row=1, column=3, value=y)
        m.set_item(row=2, column=3, value=z)

        return m

    @staticmethod
    def scaling_transform(x=1, y=1, z=1):
        # Scaling matrix is:
        # | x 0 0 0 |
        # | 0 y 0 0 |
        # | 0 0 z 0 |
        # | 0 0 0 1 |

        m = Matrix(rows=4, columns=4)
        m.set_item(row=0, column=0, value=x)
        m.set_item(row=1, column=1, value=y)
        m.set_item(row=2, column=2, value=z)
        m.set_item(row=3, column=3, value=1.0)

        return m

    @staticmethod
    def rotation_x_transform(radians=0):
        # Rotation around x axis is:
        # |    1       0       0       0    |
        # |    0     cos(r) -sin(r)    0    |
        # |    0     sin(r)  cos(r)    0    |
        # |    0       0       0       1    |

        cosine = math.cos(radians)
        sine = math.sin(radians)

        m = Matrix(rows=4, columns=4)
        m.set_item(row=0, column=0, value=1.0)
        m.set_item(row=1, column=1, value=cosine)
        m.set_item(row=1, column=2, value=-sine)
        m.set_item(row=2, column=1, value=sine)
        m.set_item(row=2, column=2, value=cosine)
        m.set_item(row=3, column=3, value=1.0)

        return m

    @staticmethod
    def rotation_y_transform(radians=0):
        # Rotation around y axis is:
        # |  cos(r)    0     sin(r)    0    |
        # |    0       1       0       0    |
        # | -sin(r)    0     cos(r)    0    |
        # |    0       0       0       1    |

        cosine = math.cos(radians)
        sine = math.sin(radians)

        m = Matrix(rows=4, columns=4)
        m.set_item(row=0, column=0, value=cosine)
        m.set_item(row=0, column=2, value=sine)
        m.set_item(row=1, column=1, value=1.0)
        m.set_item(row=2, column=0, value=-sine)
        m.set_item(row=2, column=2, value=cosine)
        m.set_item(row=3, column=3, value=1.0)

        return m

    @staticmethod
    def rotation_z_transform(radians=0):
        # Rotation around z matrix is:
        # |  cos(r) -sin(r)    0       0    |
        # |  sin(r)  cos(r)    0       0    |
        # |    0       0       1       0    |
        # |    0       0       0       1    |

        cosine = math.cos(radians)
        sine = math.sin(radians)

        m = Matrix(rows=4, columns=4)
        m.set_item(row=0, column=0, value=cosine)
        m.set_item(row=0, column=1, value=-sine)
        m.set_item(row=1, column=0, value=sine)
        m.set_item(row=1, column=1, value=cosine)
        m.set_item(row=2, column=2, value=1.0)
        m.set_item(row=3, column=3, value=1.0)

        return m

    @staticmethod
    def shearing_transform(x_moved_in_proportion_to_y=0,
                           x_moved_in_proportion_to_z=0,
                           y_moved_in_proportion_to_x=0,
                           y_moved_in_proportion_to_z=0,
                           z_moved_in_proportion_to_x=0,
                           z_moved_in_proportion_to_y=0):
        # Shearing matrix is:
        # |   1   x(y) x(z)  0   |
        # |  y(x)  1   y(z)  0   |
        # |  z(x) z(y)  1    0   |
        # |   0    0    0    1   |
        #
        # Where x(y) is x_moved_in_proportion_to_y, etc.

        m = Matrix.identity(dimensions=4)
        m.set_item(row=0, column=1, value=x_moved_in_proportion_to_y)
        m.set_item(row=0, column=2, value=x_moved_in_proportion_to_z)
        m.set_item(row=1, column=0, value=y_moved_in_proportion_to_x)
        m.set_item(row=1, column=2, value=y_moved_in_proportion_to_z)
        m.set_item(row=2, column=0, value=z_moved_in_proportion_to_x)
        m.set_item(row=2, column=1, value=z_moved_in_proportion_to_y)

        return m

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def _validate_element(self, row=0, column=0):
        if row < 0 or row >= self._rows:
            raise ValueError("Matrix row {} is out of bounds".format(row))

        if column < 0 or column >= self._columns:
            raise ValueError("Matrix column {} is out of bounds".format(column))

    def _multiply_by_matrix(self, other):
        # Currently, as a simplification, we are only going to support 4x4
        # matrix multiplication
        if self._rows !=4 or self._columns != 4 or other._rows != 4 or other._columns != 4:
            raise NotImplementedError("Only 4x4 matrix multiplication supported")

        result = Matrix(rows=self._rows, columns=other._columns)

        # For each resulting matrix row compute all of the column values
        for row in range(self._rows):
            for column in range(self._columns):
                result.set_item(row=row,
                                column=column,
                                value=self.get_item(row=row, column=0) *
                                      other.get_item(row=0, column=column) +
                                      self.get_item(row=row, column=1) *
                                      other.get_item(row=1, column=column) +
                                      self.get_item(row=row, column=2) *
                                      other.get_item(row=2, column=column) +
                                      self.get_item(row=row, column=3) *
                                      other.get_item(row=3, column=column))

        return result

    def _multiply_by_tuple(self, other):
        # Currently, as a simplification, we are only going to support
        # multiplying 4x4 matrix by a tuple.
        if self._rows != 4 or self._columns != 4:
            raise NotImplementedError("Only 4x4 matrix multiplication by 4-tuple supported")

        values = [0, 0, 0, 0]

        for row in range(self._rows):
            values[row] = self.get_item(row=row, column=0) * other.x + \
                          self.get_item(row=row, column=1) * other.y + \
                          self.get_item(row=row, column=2) * other.z + \
                          self.get_item(row=row, column=3) * other.w

        return Tuple(x=values[0], y=values[1], z=values[2], w=values[3])

    def __eq__(self, other):
        if self._rows == other._rows and self._columns == other._columns:
            return all([Utilities.equal(self._values[index], other._values[index])
                        for index in range(len(self._values))])

        return False

    def __ne__(self, other):
        return not self == other

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self._multiply_by_matrix(other)

        if isinstance(other, Tuple):
            return self._multiply_by_tuple(other)

        raise ValueError("Unable to multiply matrix by {}".format(type(other).__name__))

    def get_item(self, row=0, column=0):
        self._validate_element(row=row, column=column)

        return self._values[row * self._columns + column]

    def set_item(self, row=0, column=0, value=0.0):
        self._validate_element(row=row, column=column)

        self._values[row * self._columns + column] = value

    def transpose(self):
        transpose = Matrix(rows=self._columns, columns=self._rows)
        for row in range(transpose.rows):
            for column in range(transpose.columns):
                transpose.set_item(row=row,
                                   column=column,
                                   value=self.get_item(row=column, column=row))

        return transpose

    def determinant(self):
        if self._rows != self._columns:
            raise ValueError("Only square matrices have a determinant")

        # For a 2x2 matrix | a  c |
        #                  | b  d |
        # The determinant is simply a*d = b*c
        if self._rows == 2:
            return self.get_item(row=0, column=0) * self.get_item(row=1, column=1) - \
                   self.get_item(row=0, column=1) * self.get_item(row=1, column=0)

        # For other matrices, the determinant is computed by picking a row and
        # multiplying each element in the row by its cofactor
        determinant = 0.0
        for column in range(self._columns):
            determinant += self.get_item(row=0, column=column) * \
                           self.cofactor(row=0, column=column)
        return determinant

    def submatrix(self, row_to_remove=0, column_to_remove=0):
        submatrix = Matrix(rows=self._rows - 1, columns=self._columns - 1)

        # Copy the values from the matrix to the submatrix, making sure to skip
        # over the row and column to remove
        for row in range(submatrix.rows):
            for column in range(submatrix.columns):
                submatrix.set_item(row=row,
                                   column=column,
                                   value=self.get_item(row=row + (1 if row >= row_to_remove else 0),
                                                       column=column + (1 if column >= column_to_remove else 0)))

        return submatrix

    def minor(self, row=0, column=0):
        return self.submatrix(row_to_remove=row, column_to_remove=column).determinant()

    def cofactor(self, row=0, column=0):
        minor = self.minor(row=row, column=column)
        return minor * (1 if (((row + column) % 2) == 0) else -1)

    def inverse(self):
        determinant = self.determinant()
        if Utilities.equal(determinant, 0):
            raise ArithmeticError("Matrix is not invertible")

        # Given a matrix, for example the 4x4 matrix:
        #
        # | -5  2  6 -8 |
        # |  1 -5  1  8 |
        # |  7  7 -6 -7 |
        # |  1 -3  7  4 |
        #
        # Computing a matrix inversion consists of:
        # 1. Computing an equivalent-sized matrix that consists of the cofactors
        #    of each entry in the matrix.
        #
        # | -5  2  6 -8 |    |  116  -430   -42  -278 |
        # |  1 -5  1  8 | => |  240  -775  -119  -433 |
        # |  7  7 -6 -7 |    |  128  -236   -28  -160 |
        # |  1 -3  7  4 |    |  -24   277   105   163 |
        #
        # 2. Transposing the cofactor matrix.
        #
        # |  116  -430   -42  -278 |    |  116   240   128   -24 |
        # |  240  -775  -119  -433 | => | -430  -775  -236   277 |
        # |  128  -236   -28  -160 |    |  -42  -119   -28   105 |
        # |  -24   277   105   163 |    | -278  -433  -160   163 |
        #
        # 3. Divide each entry by the determinant of the matrix
        #
        # |  116   240   128   -24 |          |  0.21805  0.45113  0.24060 -0.04511 |
        # | -430  -775  -236   277 | / 532 => | -0.80827 -1.45677 -0.44361  0.52068 |
        # |  -42  -119   -28   105 |          | -0.07895 -0.22368 -0.05263  0.19737 |
        # | -278  -433  -160   163 |          | -0.52256 -0.81391 -0.30075  0.30639 |
        #
        # The actual implementation combines some of this and does not compute
        # the intermediate matrices.  Instead, what it will do is create a new
        # matrix of the same size.  The for each entry in this matrix, compute
        # the cofactor for the entry, divide by the determinant, and then put
        # the result in the correct entry of the transposed matrix.

        inverse = Matrix(rows=self._rows, columns=self._columns)

        for row in range(self._rows):
            for column in range(self._columns):
                inverse.set_item(row=column,
                                 column=row,
                                 value=self.cofactor(row=row, column=column) / determinant)

        return inverse

    def translate(self, x=0, y=0, z=0):
        return Matrix.translation_transform(x=x, y=y, z=z) * self

    def scale(self, x=1, y=1, z=1):
        return Matrix.scaling_transform(x=x, y=y, z=z) * self

    def rotate_x(self, radians=0):
        return Matrix.rotation_x_transform(radians=radians) * self

    def rotate_y(self, radians=0):
        return Matrix.rotation_y_transform(radians=radians) * self

    def rotate_z(self, radians=0):
        return Matrix.rotation_z_transform(radians=radians) * self

    def shear(self,
              x_moved_in_proportion_to_y=0,
              x_moved_in_proportion_to_z=0,
              y_moved_in_proportion_to_x=0,
              y_moved_in_proportion_to_z=0,
              z_moved_in_proportion_to_x=0,
              z_moved_in_proportion_to_y=0):
        return \
            Matrix.shearing_transform(x_moved_in_proportion_to_y=x_moved_in_proportion_to_y,
                                      x_moved_in_proportion_to_z=x_moved_in_proportion_to_z,
                                      y_moved_in_proportion_to_x=y_moved_in_proportion_to_x,
                                      y_moved_in_proportion_to_z=y_moved_in_proportion_to_z,
                                      z_moved_in_proportion_to_x=z_moved_in_proportion_to_x,
                                      z_moved_in_proportion_to_y=z_moved_in_proportion_to_y) * \
            self

