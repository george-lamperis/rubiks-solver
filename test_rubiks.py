import unittest
import numpy

from rubiks import S8

class TestS8(unittest.TestCase):

    def test_init(self):
        mat = numpy.matrix(numpy.identity(8), numpy.dtype(int))
        mat[:, [0, 1]] = mat[:, [1, 0]]
        mat[:, [1, 2]] = mat[:, [2, 1]]
        mat[:, [2, 3]] = mat[:, [3, 2]]

        s = S8('(1 2 3)(3 4)')
        numpy.testing.assert_equal(s.mat, mat)

    def test_equals(self):
        a = S8('(1 2 3)')
        b = S8('(1 2)')

        self.assertEqual(a, a)
        self.assertEqual(b, b)
        self.assertNotEqual(a, b)

    def test_multiply(self):
        a = S8('(1 2)')
        b = S8('(2 3)')
        c = S8('(1 3)')

        self.assertEqual(a*b, S8('(1 2 3)'))
        self.assertEqual(a*c, S8('(1 3 2)'))
        self.assertEqual(b*c, S8('(1 2 3)'))

    def test_power(self):
        a = S8('(1 2 3)')

        self.assertEqual(a**2, S8('(1 3 2)'))
        self.assertEqual(a**-1, S8('(1 3 2)'))
        self.assertEqual(a**3, S8())

    def test_of(self):
        a = S8('(1 2 3)')

        self.assertEqual(a.of(1), 2)
        self.assertEqual(a.of(2), 3)
        self.assertEqual(a.of(3), 1)

        for i in range(4, 9):
            with self.subTest(i=i):
                self.assertEqual(a.of(i), i)

    def test_str(self):
        a = S8('(3 2 1)')
        self.assertEqual(a.__str__(), '(1 3 2)')

        b = S8('(4 5 6)(1 2 3)')
        self.assertEqual(a.__str__(), '(1 2 3)(4 5 6)')
