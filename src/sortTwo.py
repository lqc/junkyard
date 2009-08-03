#! /usr/bin/python
import timeit


a = """
from math import sin

class prange(object):
    class piter(object):
        def __init__(self, cont):
            self.iter = iter(cont)

        def __iter__(self):
            return self

        def next(self):
            return sin(self.iter.next())
        
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self.piter(xrange(self.n))"""

print timeit.timeit("[sin(x) for x in xrange(10000)]", "from math import sin", number=100)
print timeit.timeit("list(prange(10000))", a, number=100)
print timeit.timeit("list(xrange(10000))", number=100)

