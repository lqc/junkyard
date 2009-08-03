#!/usr/bin/env python

import timeit

if_not="if 0!=1: None"

if_nor='if not 0: None'

if_fal="if False: None"

t=timeit.Timer(stmt=if_not)
print "If not: ",t.timeit(1000000)

t=timeit.Timer(stmt=if_nor)
print "If !=:",t.timeit(1000000)

t=timeit.Timer(stmt=if_fal)
print "If False:",t.timeit(1000000)

