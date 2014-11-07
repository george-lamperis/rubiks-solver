"""
TODO: Rename Permutation. Sn(n, string)?

Solve with Petrus Method
"""

import numpy


class Permutation:
    """
    These permutations evaluate right to left, just like functions and matrices.

    TODO operators assert matching size
         dtype = integer or bool maybe?
         use matlib.identity instead
         make sure we make deep copies
    """

    def __init__(self, size, string=None):
        """ If string=None, return identity permutation. """
        self.size = size
        self.mat = numpy.matrix(numpy.identity(self.size), numpy.dtype(int))

        if string:
            cycles = string.replace('(', '').split(')')
            swaps = []

            # convert to indices
            for c in cycles:
                l = [int(x)-1 for x in c.split()]
                swaps += list(zip(l, l[1:]))

            # product of 2-cycles
            for i, j in swaps:
                m = numpy.matrix(numpy.identity(self.size), numpy.dtype(int))
                m[:, [i, j]] = m[:, [j, i]]
                self.mat = self.mat * m

    def __eq__(self, other):
        return (self.mat == other.mat).all()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        if self.size != other.size:
            raise TypeError('sizes not equal')

        product = Permutation(self.size)
        product.mat = self.mat * other.mat
        return product

    def __pow__(self, n):
        result = Permutation(self.size)
        result.mat = self.mat ** n
        return result

    def __str__(self):
        """ ordered alphabetically. """
        s = ''
        domain = list(range(1, self.size+1))
        while domain:
            start = domain.pop(0)
            i = self.of(start)

            if i != start:
                s +='({}'.format(start)
                while i != start:
                    s += ' {}'.format(i)
                    idx = domain.index(i)
                    domain.pop(idx)
                    i = self.of(i)

                s += ')'

        return s

    def of(self, n):
        for i, x in enumerate(self.mat[:, n-1].flat, start=1):
            if x:
                return i

    def is_identity(self):
        return self == Permutation(self.size)

    def inverse(self):
        return self ** -1

class CornerOrientation():

    def __init__(x=None):
        """ x should be an 8-tuple with elements in Z/3. """
        if x:
            self.x = x
        else:
            self.x = (0, 0, 0, 0, 0, 0, 0, 0)

    def D(self):
        pass

    def U(self):
        pass

    def L(self):
        pass

    def R(self):
        pass

    def F(self):
        pass

    def B(self):
        pass

class EdgeOrientation():

    def __init__(y=None):
        """ y should be an 12-tuple with elements in Z/2. """
        if y:
            self.y = y
        else:
            self.y = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def D(self):
        pass

    def U(self):
        pass

    def L(self):
        pass

    def R(self):
        pass

    def F(self):
        pass

    def B(self):
        pass

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

