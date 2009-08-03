#! /usr/bin/python
import timeit

t=timeit.Timer("[2*x for x in range(10000)]")
print("range: ",t.timeit(2000))

t=timeit.Timer("list(range(10000))")
print("list(range()): ",t.timeit(2000))