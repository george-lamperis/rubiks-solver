"""
TODO: Rename Permutation. Sn(n, string)?

Solve with Petrus Method
"""

import numpy


class S8:
    """
    These permutations evaluate right to left, just like functions and matrices.
    """

    def __init__(self, string=None):
        """ If string=None, return identity permutation. """
        self.mat = numpy.matrix(numpy.identity(8))

        if string:
            cycles = string.replace('(', '').split(')')
            swaps = []

            # convert to indices
            for c in cycles:
                l = [int(x)-1 for x in c.split()]
                swaps += list(zip(l, l[1:]))

            # product of 2-cycles
            for i, j in swaps:
                m = numpy.matrix(numpy.identity(8))
                m[:, [i, j]] = m[:, [j, i]]
                self.mat = self.mat * m

    def __eq__(self, other):
        return (self.mat == other.mat).all()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        # assert S8?
        product = S8()
        product.mat = self.mat * other.mat
        return product

    def __pow__(self, n):
        # assert integer?
        return self.mat ** n

    def __str__(self):
        pass

    def of(self, n):
        pass


class S12:
    corners =['ufl', 'urf', 'ubr', 'ulb', 'dbl', 'dlf', 'dfr', 'drb']
    edges = ['ub', 'ur', 'uf', 'ul', 'lb', 'rb', 'rf', 'lf', 'db', 'dr', 'df', 'dl']

class State:

    def __init__(self):
        pass

    @classmethod
    def initial_state(cls):
        pass

    def __str__(self):
        pass

    def _is_valid(self):
        pass


    def F(self):
        pass

    def f(self):
        pass

if __name__ == "__main__":
    print('hello world!')

