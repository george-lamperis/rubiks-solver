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

    def __init__(self, x=None):
        """ x should be an 8-tuple with elements in Z/3. """
        if x:
            self.x = x
        else:
            self.x = (0, 0, 0, 0, 0, 0, 0, 0)

    def __eq__(self, other):
        return self.x == other.x

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.x)

    def _manipulate(self, lst):
        """ (position, add) """
        l = []
        for i, addend in lst:
           l.append((self.x[i-1] + addend) % 3)

        return tuple(l)

    def D(self):
        # (x1 , x2, x3, x4, x8, x5, x6  x7)
        ops = [(1, 0), (2, 0), (3, 0), (4, 0), (8, 0), (5, 0), (6, 0), (7, 0)]
        t = self._manipulate(ops)
        return CornerOrientation(t)

    def U(self):
        # (x2, x3, x4, x1, x5, x6, x7, x8)
        ops = [(2, 0), (3, 0), (4, 0), (1, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
        t = self._manipulate(ops)
        return CornerOrientation(t)

    def R(self):
        # (x1, x7 + 1, x2 + 2, x4, x5, x6, x8 + 2, x3 + 1)
        ops = [(1, 0), (7, 1), (2, 2), (4, 0), (5, 0), (6, 0), (8, 2), (3, 1)]
        t = self._manipulate(ops)
        return CornerOrientation(t)

    def L(self):
        # (x4 + 2, x2, x3, x5 + 1, x6 + 2, x1 + 1, x7, x8)
        ops = [(4, 2), (2, 0), (3, 0), (5, 1), (6, 2), (1, 1), (7, 0), (8, 0)]
        t = self._manipulate(ops)
        return CornerOrientation(t)

    def F(self):
        # (x6 + 1, x1 + 2, x3, x4, x5 , x7 + 2, x2 + 1, x8)
        ops = [(6, 1), (1, 2), (3, 0), (4, 0), (5, 0), (7, 2), (2, 1), (8, 0)]
        t = self._manipulate(ops)
        return CornerOrientation(t)

    def B(self):
        # (x1, x2, x8 + 1, x3 + 2, x4 + 1, x6, x7, x5 + 2)
        ops = [(1, 0), (2, 0), (8, 1), (3, 2), (4, 1), (6, 0), (7, 0), (5, 2)]
        t = self._manipulate(ops)
        return CornerOrientation(t)

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
    # How will we represent the rotation of the cube? (Colors)

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

