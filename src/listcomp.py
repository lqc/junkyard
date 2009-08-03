L = []
def pierwsze(n):
    global L
    L = [(x, True) for x in xrange(1,n+1)]

    def wykresl(n):
        global L
        L = L[0:n-1] + [ (p[0], p[1] and (p[0] % n != 0)) for p in L[n-1:]]        
        return True

    return [ L[i][0] for i in xrange(1,n) if (L[i][1] and wykresl(L[i][0]))]
# print pierwsze(23)

from math import log
def is_prime(n):
    if n == 1: return False
    for i in xrange(2, n/2):
        if n % i == 0:
            return False
    return True

def doskonale(n):
    s = [0]
    def add(s, k):
        s[0] += k
        return s[0]    
    return [ p[0]*p[1] for p in [(2**k, add(s, 2**k) ) for k in xrange(0, int(log(n,2))) if s[0]*2**k < n] if is_prime(p[1]) ]

print doskonale(33550337)

