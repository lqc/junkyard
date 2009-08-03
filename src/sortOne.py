#! /usr/bin/python
import time
import functools
import itertools
import operator

N = 100

def fold(f, iter):
    iter = iter.__iter__()
    r = ''
    try:
        r = f(r, iter.next())
        while True:
            r = f(r, iter.next())
    except StopIteration:
        return r
    

start = time.time()
for i in xrange(N):
    ' '.join(map(str, xrange(1, 100000)))
end = time.time()
print (end - start)/N, "total: ", (end - start)

start = time.time()
for i in xrange(N):
    ' '.join(itertools.imap(str, xrange(1, 100000)))
end = time.time()
print (end - start)/N, "total: ", (end - start)

g = ( str(e) for e in xrange(1,100000) )

start = time.time()
for i in xrange(N):
    ' '.join(g)
end = time.time()

print (end - start)/N, "total: ", (end - start)


