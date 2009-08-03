import sys
import time
import random
from rbt import TreeMap
import sys

minor = sys.version_info[0]
if minor >= 3:
  xrange = range

def rbt_bm():
  n = 100000
  a1 = [random.randint(0, 999999) for x in xrange(0, n)]
  tree = TreeMap()
  tree2 = TreeMap()

  start = time.time()

  for i in xrange(0, n):
    tree[i] = i
  for i in xrange(0, n):
    del tree[i]
  
  for x in a1:
    tree2[x] = x

  for x in reversed(a1):
    tree2[x]
    
  for key in reversed(tree2):
    key
      
  for key in tree2:
    key

    
  for i in xrange(0, n):
    tree2.max_key()

  for i in xrange(0, n):
    tree2.min_key()

  return time.time() - start

#import cProfile
#cProfile.run("rbt_bm()", "profile.out")

if len(sys.argv) > 1:
  n = int(sys.argv[1])
else:
  n = 5
for i in xrange(0, n):
  print("%02f" % rbt_bm())

