import unittest
import numpy

from rubiks import Permutation
from rubiks import CornerOrientation

class TestPermutation(unittest.TestCase):

    def test_init(self):
        mat = numpy.matlib.identity(8)
        mat[:, [0, 1]] = mat[:, [1, 0]]
        mat[:, [1, 2]] = mat[:, [2, 1]]
        mat[:, [2, 3]] = mat[:, [3, 2]]

        s = Permutation(8, '(1 2 3)(3 4)')
        numpy.testing.assert_equal(s.mat, mat)

    def test_equals(self):
        a = Permutation(8, '(1 2 3)')
        b = Permutation(8, '(1 2)')

        self.assertEqual(a, a)
        self.assertEqual(b, b)
        self.assertNotEqual(a, b)

    def test_multiply(self):
        a = Permutation(8, '(1 2)')
        b = Permutation(8, '(2 3)')
        c = Permutation(8, '(1 3)')

        self.assertEqual(a*b, Permutation(8, '(1 2 3)'))
        self.assertEqual(a*c, Permutation(8, '(1 3 2)'))
        self.assertEqual(b*c, Permutation(8, '(1 2 3)'))

    def test_power(self):
        a = Permutation(8, '(1 2 3)')

        self.assertEqual(a**2, Permutation(8, '(1 3 2)'))
        self.assertEqual(a**-1, Permutation(8, '(1 3 2)'))
        self.assertEqual(a**3, Permutation(8))

    def test_of(self):
        a = Permutation(8, '(1 2 3)')

        self.assertEqual(a.of(1), 2)
        self.assertEqual(a.of(2), 3)
        self.assertEqual(a.of(3), 1)

        for i in range(4, 9):
            with self.subTest(i=i):
                self.assertEqual(a.of(i), i)

    def test_str(self):
        # a = Permutation(8)
        # self. assertEqual(a.__str__(), '(1)')

        b = Permutation(8, '(3 2 1)')
        self.assertEqual(b.__str__(), '(1 3 2)')

        c = Permutation(8, '(4 5 6)(1 2 3)')
        self.assertEqual(c.__str__(), '(1 2 3)(4 5 6)')

    def test_is_identity(self):
        a = Permutation(8)
        self.assertTrue(a.is_identity())

        b = Permutation(8, '(1 2)')
        self.assertFalse(b.is_identity())

    def test_inverse(self):
        self.assertEqual(Permutation(8, '(1 2 3)').inverse(), Permutation(8, '(1 3 2)'))
        self.assertEqual(Permutation(8, '(1 2)').inverse(), Permutation(8, '(1 2)'))

    def test_order(self):
        pass

    def test_raises_type_error(self):
        a = Permutation(2)
        b = Permutation(3)

        with self.assertRaises(TypeError):
            a * b

    def test_of_out_of_bounds(self):
        pass

class TestCornerOrientation(unittest.TestCase):

    def test_init(self):
        pass

    def test_D(self):
        actual = CornerOrientation((0, 0, 0, 0, 1, 2, 1, 0)).D()
        expected = CornerOrientation((0, 0, 0, 0, 0, 1, 2, 1))
        self.assertEqual(actual, expected)

    def test_U(self):
        actual = CornerOrientation((1, 2, 1, 0, 0, 0, 0, 0)).U()
        expected = CornerOrientation((2, 1, 0, 1, 0, 0, 0, 0))
        self.assertEqual(actual, expected)

    def test_R(self):
        actual = CornerOrientation((0, 1, 2, 0, 1, 2, 0, 1)).R()
        expected = CornerOrientation((0, 1, 0, 0, 1, 2, 0, 0))
        self.assertEqual(actual, expected)

    def test_L(self):
        actual = CornerOrientation((0, 1, 2, 0, 1, 2, 0, 1)).L()
        expected = CornerOrientation((2, 1, 2, 2, 1, 1, 0, 1))
        self.assertEqual(actual, expected)

    def test_F(self):
        actual = CornerOrientation((0, 1, 2, 0, 1, 2, 0, 1)).F()
        expected = CornerOrientation((0, 2, 2, 0, 1, 2, 2, 1))
        self.assertEqual(actual, expected)

    def test_B(self):
        actual = CornerOrientation((0, 1, 2, 0, 1, 2, 0, 1)).B()
        expected = CornerOrientation((0, 1, 2, 1, 1, 2, 0, 0))
        self.assertEqual(actual, expected)
