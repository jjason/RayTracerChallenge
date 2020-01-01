import unittest

from matrix import Matrix
from tuple import Tuple
from util import Utilities


class TestMatrix(unittest.TestCase):
    def test_default_create(self):
        m = Matrix(rows=4, columns=4)
        self.assertEqual(m.rows, 4)
        self.assertEqual(m.columns, 4)
        self.assertTrue(all([Utilities.equal(m.get_item(row=row, column=column), 0)
                             for column in range(m.columns)
                             for row in range(m.rows)]))

    def test_create_4x4(self):
        m = Matrix(rows=4, columns=4, values=[1, 2, 3, 4,
                                              5.5, 6.5, 7.5, 8.5,
                                              9, 10, 11, 12,
                                              13.5, 14.5, 15.5, 16.5])
        self.assertEqual(m.rows, 4)
        self.assertEqual(m.columns, 4)
        self.assertTrue(Utilities.equal(m.get_item(row=0, column=0), 1))
        self.assertTrue(Utilities.equal(m.get_item(row=0, column=3), 4))
        self.assertTrue(Utilities.equal(m.get_item(row=1, column=0), 5.5))
        self.assertTrue(Utilities.equal(m.get_item(row=1, column=2), 7.5))
        self.assertTrue(Utilities.equal(m.get_item(row=2, column=2), 11))
        self.assertTrue(Utilities.equal(m.get_item(row=3, column=0), 13.5))
        self.assertTrue(Utilities.equal(m.get_item(row=3, column=2), 15.5))

    def test_create_2x2(self):
        m = Matrix(rows=2, columns=2, values=[-3, 5,
                                              1, -2])
        self.assertEqual(m.rows, 2)
        self.assertEqual(m.columns, 2)
        self.assertTrue(Utilities.equal(m.get_item(row=0, column=0), -3))
        self.assertTrue(Utilities.equal(m.get_item(row=0, column=1), 5))
        self.assertTrue(Utilities.equal(m.get_item(row=1, column=0), 1))
        self.assertTrue(Utilities.equal(m.get_item(row=1, column=1), -2))

    def test_create_3x3(self):
        m = Matrix(rows=3, columns=3, values=[-3, 5, 0,
                                              1, -2, -7,
                                              0, 1, 1])
        self.assertEqual(m.rows, 3)
        self.assertEqual(m.columns, 3)
        self.assertTrue(Utilities.equal(m.get_item(row=0, column=0), -3))
        self.assertTrue(Utilities.equal(m.get_item(row=1, column=1), -2))
        self.assertTrue(Utilities.equal(m.get_item(row=2, column=2), 1))

    def test_equality_with_equal_matrices(self):
        m1 = Matrix(rows=4, columns=4, values=[1, 2, 3, 4,
                                               5, 6, 7, 8,
                                               9, 10, 11, 12,
                                               13, 14, 15, 16])
        m2 = Matrix(rows=4, columns=4, values=[1, 2, 3, 4,
                                               5, 6, 7, 8,
                                               9, 10, 11, 12,
                                               13, 14, 15, 16])
        self.assertTrue(m1 == m2)
        self.assertFalse(m1 != m2)

    def test_equality_with_unequal_matrices(self):
        m1 = Matrix(rows=4, columns=4, values=[1, 2, 3, 4,
                                               5, 6, 7, 8,
                                               9, 8, 7, 6,
                                               5, 4, 3, 2])
        m2 = Matrix(rows=4, columns=4, values=[2, 3, 4, 5,
                                               6, 7, 8, 9,
                                               8, 7, 6, 5,
                                               4, 3, 2, 1])
        self.assertFalse(m1 == m2)
        self.assertTrue(m1 != m2)

    def test_equality_with_different_size_matrices(self):
        m1 = Matrix(rows=4, columns=4, values=[1, 2, 3, 4,
                                               5, 6, 7, 8,
                                               9, 8, 7, 6,
                                               5, 4, 3, 2])
        m2 = Matrix(rows=3, columns=3, values=[1, 2, 3,
                                               4, 5, 6,
                                               7, 8, 9])
        self.assertFalse(m1 == m2)
        self.assertTrue(m1 != m2)

    def test_multiply_2x2_by_2x2(self):
        m = Matrix(rows=2, columns=2)
        with self.assertRaises(NotImplementedError):
            m * m

    def test_multiply_3x3_by_3x3(self):
        m = Matrix(rows=3, columns=3)
        with self.assertRaises(NotImplementedError):
            m * m

    def test_multiply_incompatible_sizes(self):
        m1 = Matrix(rows=4, columns=4)
        m2 = Matrix(rows=3, columns=4)
        with self.assertRaises(NotImplementedError):
            m1 * m2

    def test_multiply_4x4_by_4x4(self):
        m1 = Matrix(rows=4, columns=4, values=[1, 2, 3, 4,
                                               5, 6, 7, 8,
                                               9, 8, 7, 6,
                                               5, 4, 3, 2])
        m2 = Matrix(rows=4, columns=4, values=[-2, 1, 2, 3,
                                               3, 2, 1, -1,
                                               4, 3, 6, 5,
                                               1, 2, 7, 8])
        m3 = m1 * m2
        self.assertEqual(m3.rows, 4)
        self.assertEqual(m3.columns, 4)
        self.assertTrue(m3 == Matrix(rows=4, columns=4, values=[20, 22, 50, 48,
                                                                44, 54, 114, 108,
                                                                40, 58, 110, 102,
                                                                16, 26, 46, 42]))

    def test_multiply_2x2_by_tuple(self):
        m = Matrix(rows=2, columns=2)
        t = Tuple()
        with self.assertRaises(NotImplementedError):
            m * t

    def test_multiply_3x3_by_tuple(self):
        m = Matrix(rows=3, columns=3)
        t = Tuple()
        with self.assertRaises(NotImplementedError):
            m * t

    def test_multiply_4x4_by_tuple(self):
        m = Matrix(rows=4, columns=4, values=[1, 2, 3, 4,
                                              2, 4, 4, 2,
                                              8, 6, 4, 1,
                                              0, 0, 0, 1])
        t1 = Tuple(x=1, y=2, z=3, w=1)
        t2 = m * t1
        self.assertTrue(isinstance(t2, Tuple))
        self.assertTrue(t2 == Tuple(18, 24, 33, 1))

    def test_multiply_4x4_by_identity(self):
        m = Matrix(rows=4, columns=4, values=[0, 1, 2, 4,
                                              1, 2, 4, 8,
                                              2, 4, 8, 16,
                                              4, 8, 16, 32])
        i = Matrix.identity(dimensions=4)
        self.assertEqual(m * i, m)

    def test_transpose(self):
        m1 = Matrix(rows=4, columns=4, values=[0, 9, 3, 0,
                                               9, 8, 0, 8,
                                               1, 8, 5, 3,
                                               0, 0, 5, 8])
        t1 = Matrix(rows=4, columns=4, values=[0, 9, 1, 0,
                                               9, 8, 8, 0,
                                               3, 0, 5, 5,
                                               0, 8, 3, 8])
        self.assertEqual(m1.transpose(), t1)

        m2 = Matrix(rows=4, columns=3, values=[1, 2, 3,
                                               4, 5, 6,
                                               7, 8, 9,
                                               10, 11, 12])
        t2 = Matrix(rows=3, columns=4, values=[1, 4, 7, 10,
                                               2, 5, 8, 11,
                                               3, 6, 9, 12])
        self.assertEqual(m2.transpose(), t2)

    def test_transpose_identity(self):
        i = Matrix.identity(dimensions=4)
        self.assertEqual(i.transpose(), i)

    def test_determinant_non_square(self):
        with self.assertRaises(ValueError):
            Matrix(rows=2, columns=3).determinant()

    def test_determinant_2x2(self):
        m = Matrix(rows=2, columns=2, values=[1, 5,
                                              -3, 2])
        self.assertTrue(Utilities.equal(m.determinant(), 17))

    def test_determinant_3x3(self):
        m = Matrix(rows=3, columns=3, values=[1, 2, 6,
                                              -5, 8, -4,
                                              2, 6, 4])
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=0), 56))
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=1), 12))
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=2), -46))
        self.assertTrue(Utilities.equal(m.determinant(), -196))

    def test_determinant_4x4(self):
        m = Matrix(rows=4, columns=4, values=[-2, -8, 3, 5,
                                              -3, 1, 7, 3,
                                              1, 2, -9, 6,
                                              -6, 7, 7, -9])
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=0), 690))
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=1), 447))
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=2), 210))
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=3), 51))
        self.assertTrue(Utilities.equal(m.determinant(), -4071))

    def test_submatrix_3x3(self):
        m = Matrix(rows=3, columns=3, values=[1, 5, 0,
                                              -3, 2, 7,
                                              0, 6, -3])
        s00 = Matrix(rows=2, columns=2, values=[2, 7,
                                                6, -3])
        self.assertEqual(m.submatrix(row_to_remove=0, column_to_remove=0), s00)

        s01 = Matrix(rows=2, columns=2, values=[-3, 7,
                                                0, -3])
        self.assertEqual(m.submatrix(row_to_remove=0, column_to_remove=1), s01)

        s02 = Matrix(rows=2, columns=2, values=[-3, 2,
                                                0, 6])
        self.assertEqual(m.submatrix(row_to_remove=0, column_to_remove=2), s02)

        s10 = Matrix(rows=2, columns=2, values=[5, 0,
                                                6, -3])
        self.assertEqual(m.submatrix(row_to_remove=1, column_to_remove=0), s10)

        s11 = Matrix(rows=2, columns=2, values=[1, 0,
                                                0, -3])
        self.assertEqual(m.submatrix(row_to_remove=1, column_to_remove=1), s11)

        s12 = Matrix(rows=2, columns=2, values=[1, 5,
                                                0, 6])
        self.assertEqual(m.submatrix(row_to_remove=1, column_to_remove=2), s12)

        s20 = Matrix(rows=2, columns=2, values=[5, 0,
                                                2, 7])
        self.assertEqual(m.submatrix(row_to_remove=2, column_to_remove=0), s20)

        s21 = Matrix(rows=2, columns=2, values=[1, 0,
                                                -3, 7])
        self.assertEqual(m.submatrix(row_to_remove=2, column_to_remove=1), s21)

        s22 = Matrix(rows=2, columns=2, values=[1, 5,
                                                -3, 2])
        self.assertEqual(m.submatrix(row_to_remove=2, column_to_remove=2), s22)

    def test_submatrix_4x4(self):
        m = Matrix(rows=4, columns=4, values=[-6, 1, 1, 6,
                                              -8, 5, 8, 6,
                                              -1, 0, 8, 2,
                                              -7, 1, -1, 1])
        s00 = Matrix(rows=3, columns=3, values=[5, 8, 6,
                                                0, 8, 2,
                                                1, -1, 1])
        self.assertEqual(m.submatrix(row_to_remove=0, column_to_remove=0), s00)

        s11 = Matrix(rows=3, columns=3, values=[-6, 1, 6,
                                                -1, 8, 2,
                                                -7, -1, 1])
        self.assertEqual(m.submatrix(row_to_remove=1, column_to_remove=1), s11)

        s22 = Matrix(rows=3, columns=3, values=[-6, 1, 6,
                                                -8, 5, 6,
                                                -7, 1, 1])
        self.assertEqual(m.submatrix(row_to_remove=2, column_to_remove=2), s22)

        s33 = Matrix(rows=3, columns=3, values=[-6, 1, 1,
                                                -8, 5, 8,
                                                -1, 0, 8])
        self.assertEqual(m.submatrix(row_to_remove=3, column_to_remove=3), s33)

    def test_minor_3x3(self):
        m = Matrix(rows=3, columns=3, values=[3, 5, 0,
                                              2, -1, -7,
                                              6, -1, 5])
        s = m.submatrix(row_to_remove=1, column_to_remove=0)
        self.assertTrue(Utilities.equal(s.determinant(), 25))
        self.assertTrue(Utilities.equal(m.minor(row=1, column=0), 25))

    def test_cofactor_3x3(self):
        m = Matrix(rows=3, columns=3, values=[3, 5, 0,
                                              2, -1, -7,
                                              6, -1, 5])
        self.assertTrue(Utilities.equal(m.minor(row=0, column=0), -12))
        self.assertTrue(Utilities.equal(m.cofactor(row=0, column=0), -12))
        self.assertTrue(Utilities.equal(m.minor(row=1, column=0), 25))
        self.assertTrue(Utilities.equal(m.cofactor(row=1, column=0), -25))

    def test_determinant_invertible_matrix(self):
        m = Matrix(rows=4, columns=4, values=[6, 4, 4, 4,
                                              5, 5, 7, 6,
                                              4, -9, 3, -7,
                                              9, 1, 7, -6])
        self.assertTrue(Utilities.equal(m.determinant(), -2120))

    def test_determinant_noninvertible_matrix(self):
        m = Matrix(rows=4, columns=4, values=[-4, 2, -2, -3,
                                              9, 6, 2, 6,
                                              0, -5, 1, -5,
                                              0, 0, 0, 0])
        self.assertTrue(Utilities.equal(m.determinant(), 0))

    def test_inverse_noninvertible_matrix(self):
        m = Matrix(rows=4, columns=4, values=[-4, 2, -2, -3,
                                              9, 6, 2, 6,
                                              0, -5, 1, -5,
                                              0, 0, 0, 0])
        with self.assertRaises(ArithmeticError):
            m.inverse()

    def test_inverse_4x4_matrix(self):
        m = Matrix(rows=4, columns=4, values=[-5, 2, 6, -8,
                                              1, -5, 1, 8,
                                              7, 7, -6, -7,
                                              1, -3, 7, 4])
        i = m.inverse()
        self.assertTrue(Utilities.equal(m.determinant(), 532))
        self.assertTrue(Utilities.equal(m.cofactor(row=2, column=3), -160))
        self.assertTrue(Utilities.equal(i.get_item(row=3, column=2), -160/532))
        self.assertTrue(Utilities.equal(m.cofactor(row=3, column=2), 105))
        self.assertTrue(Utilities.equal(i.get_item(row=2, column=3), 105/532))
        self.assertEqual(i, Matrix(rows=4, columns=4, values=[0.21805, 0.45113, 0.24060, -0.04511,
                                                              -0.80827, -1.45677, -0.44361, 0.52068,
                                                              -0.07895, -0.22368, -0.05263, 0.19737,
                                                              -0.52256, -0.81391, -0.30075, 0.30639]))

        m = Matrix(rows=4, columns=4, values=[8, -5, 9, 2,
                                              7, 5, 6, 1,
                                              -6, 0, 9, 6,
                                              -3, 0, -9, -4])
        i = m.inverse()
        self.assertEqual(i, Matrix(rows=4, columns=4, values=[-0.15385, -0.15385, -0.28205, -0.53846,
                                                              -0.07692, 0.12308, 0.02564, 0.03077,
                                                              0.35897, 0.35897, 0.43590, 0.92308,
                                                              -0.69231, -0.69231, -0.76923, -1.92308]))

        m = Matrix(rows=4, columns=4, values=[9, 3, 0, 9,
                                              -5, -2, -6, -3,
                                              -4, 9, 6, 4,
                                              -7, 6, 6, 2])
        i = m.inverse()
        self.assertEqual(i, Matrix(rows=4, columns=4, values=[-0.04074, -0.07778, 0.14444, -0.22222,
                                                              -0.07778, 0.03333, 0.36667, -0.33333,
                                                              -0.02901, -0.14630, -0.10926, 0.12963,
                                                              0.17778, 0.06667, -0.26667, 0.33333]))

    def test_multiply_matrix_product_by_inverse(self):
        m1 = Matrix(rows=4, columns=4, values=[3, -9, 7, 3,
                                               3, -8, 2, -9,
                                               -4, 4, 4, 1,
                                               -6, 5, -1, 1])
        m2 = Matrix(rows=4, columns=4, values=[8, 2, 2, 2,
                                               3, -1, 7, 0,
                                               7, 0, 5, 4,
                                               6, 2, 0, 5])
        m3 = m1 * m2
        self.assertEqual(m3 * m2.inverse(), m1)


if __name__ == '__main__':
    unittest.main()
