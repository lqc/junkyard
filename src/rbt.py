#
# Red-Black Trees (objective style)
#
# (C) 2009 Lukasz Rekucki
#

from collections import MutableMapping

_RED = 1
_BLACK = 0

class TreeMap(MutableMapping):
    # some private class
    class TreeNode(object):
        def __init__(self, key, value, color, left, right):
            self.key = key
            self.value = value
            self.color = color
            self.left = left
            self.right = right

        def insert(self, k, v):
            if k == self.key:
                self.value = v
                return self, False

            if k < self.key:
                self.left, tag = self.left.insert(k, v)

                if self.left.color:
					if self.right.color:
						self.color = _RED
						self.left.color = self.right.color = _BLACK
					else:
						if self.left.left.color:
							return self.rotate_once_right(), tag
						elif self.left.right.color:
							return self.rotate_twice_right(), tag
            else:
                self.right, tag = self.right.insert(k, v)

                if self.right.color:
					if self.left.color:
						self.color = _RED
						self.left.color = self.right.color = _BLACK
					else:
						if self.right.right.color:
							return self.rotate_once_left(), tag
						elif self.right.left.color:
							return self.rotate_twice_left(), tag
            return self, tag

        def rotate_once_left(self):
            save = self.right
            self.right = save.left
            save.left = self
            self.color = _RED
            save.color = _BLACK
            return save

        def rotate_once_right(self):
            save = self.left
            self.left = save.right
            save.right = self
            self.color = _RED
            save.color = _BLACK
            return save

        def rotate_twice_left(self):
            self.right = self.right.rotate_once_right()
            self.right.parent = self
            return self.rotate_once_left()

        def rotate_twice_right(self):
            self.left = self.left.rotate_once_left()
            self.left.parent = self
            return self.rotate_once_right()

        def find(self, key):
            if key == self.key:
                return self
            elif key < self.key:
                return self.left.find(key)
            else:
                return self.right.find(key)

        def p(self, lvl):
			print lvl * "  " + str(self.key) + " " + str(self.value)
			self.left.p(lvl + 1)
			self.right.p(lvl + 1)

        def getchild(self, right):
            if right:
                return self.right
            else:
                return self.left

        def setchild(self, right, n):
            if right:
                self.right = n
            else:
                self.left = n

        def rotate_once(self, right):
            if right:
                return self.rotate_once_right()
            else:
                return self.rotate_once_left()
        
        def rotate_twice(self, right):
            if right:
                return self.rotate_twice_right()
            else:
                return self.rotate_twice_left()

        def delete(self, key, f, g, p, last):            
            dir = (self.key < key)
            #print self, key, f, g, p, last, dir

            if f is None and self.key == key:
                f = self

            if self.color or self.getchild(dir).color:
                # just descend
                #print "DESC 1"
                return self.getchild(dir).delete(key, f, p, self, dir)

            if self.getchild(not dir).color:
                #print "ROT 1"
                n = self.rotate_once(dir)
                p.setchild(last, n)
                p = n
            elif not self.getchild(not dir).color:
                #print "R2"
                s = p.getchild(not last)

                if s == TreeMap.NIL:
                    #print "DESC 3"
                    return self.getchild(dir).delete(key, f, p, self, dir)

                if not s.left.color and not s.right.color:
                    #print "FLIP"
                    p.color = _BLACK
                    s.color = _RED
                    self.color = _RED
                else:
                    d2 = (g.right == p)
                    if s.getchild(last).color:
                        #print "DOUBLE ROT"
                        g.setchild(d2, p.rotate_twice(last))
                    elif s.getchild(not last).color:
                        #print "SINGLE ROT"
                        g.setchild(d2, p.rotate_once(last))

                    self.color = _RED
                    x = g.getchild(d2)
                    x.color = x.left.color = x.right.color = _BLACK

            #print "DESC 4:"
            return self.getchild(dir).delete(key, f, p, self, dir)

        def collect(self, f, nil=None, order=(lambda s, l, r: (s, l, r))):
            a, b, c = order(lambda *a: [f(self)], \
                self.left.collect, self.right.collect)
            return a(f, nil, order) + b(f, nil, order) + c(f, nil, order)

        def __str__(self):
            return repr((self.key, self.value, self.color))

    class NilNode(TreeNode):
        def __init__(self, left=None, right=None):
           self.key = None
           self.value = None
           self.color = _BLACK
           self.left = left
           self.right = right

        def insert(self, key, value):
            return TreeMap.TreeNode(key, value, _RED, self, self), True

        def find(self, key):
            raise KeyError("Key %r not found in map." % key)
            pass

        def collect(self, f=None, nil=None, order=None):
            if nil is None:
                return []
            else:
                return [nil()]
            
        def __str__(self):
            return "NIL"

        def delete(self, k, f, g, p, last):
            if f is None:
                raise KeyError("Couldn't delete, key '%r' not found." % k)
            
            f.key, p.key = p.key, f.key
            f.value, p.value = p.value, f.value
            
            g.setchild(g.right == p, \
                p.getchild(p.left == TreeMap.NIL))
            return p

        def validate(self, lastc, bp):
            pass

    NIL = NilNode()

    def __init__(self):
        self.root = TreeMap.NIL
        self.fake = self.NilNode(TreeMap.NIL, self.root)
        self._size = 0

    def __setitem__(self, key, value=None):
        self.root, tag = self.root.insert(key, value)
        self.fake.right = self.root
        self.root.color = _BLACK
        if tag:
            self._size += 1

    def __getitem__(self, key):
        return self.root.find(key).value

    def __delitem__(self, key):
        n = self.root.delete(key, None, None, self.fake, True)
      
        self.root = self.fake.right
        self.root.color = _BLACK
        self._size -= 1
        return n.value

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.collect(lambda x: x.key, \
            order=lambda s, l, r: (l, s, r)).__iter__()

    def __reversed__(self):
        return self.root.collect(lambda x: x.key, \
            order=lambda s, l, r: (r, s, l)).__iter__()

    def keys(self):
        return self.root.collect(lambda x: x.key, order=lambda s, l, r: (l, s, r))

    def max_key(self):
        p = self.fake
        q = self.root
        while q != TreeMap.NIL:
            p = q
            q = q.right

        return p.key

    def min_key(self):
        p = self.fake
        q = self.root
        while q != TreeMap.NIL:
            p = q
            q = q.left

        return p.key

    def validate(self):
        self.root.validate()

    def inord_print(self):
        return '\n'.join(self.root.collect(lambda x: str(x), lambda: "NIL"))

def test():
    map = TreeMap()
    for x in xrange(1, 11):
        map[x] = "<%d>" % x

    for x in map:
        print x
    print map


if __name__ == "__main__":
	test()
