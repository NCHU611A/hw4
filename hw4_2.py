# -*- coding: utf-8 -*-
"""

第二小題

"""
import sys

# Fibonacci series using recursion
def recursive(n):
    try:
        if n <= 1:
            return n
        else:
            return recursive(n-1) + recursive(n-2)
    except MemoryError:
        print("recursive MemoryError: n = {} is too large.".format(n))
        dynamic_programming(n)
        sys.exit(0)
        
# Fibonacci Series using Dynamic Programming
def dynamic_programming(n):
    try:
        # Taking 1st two fibonacci numbers as 0 and 1
        f = [0, 1]
         
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
        
        return f[n]
    except MemoryError:
        print("dynamic_programming MemoryError: n = {} is too large.".format(n))    
        
for n in range(1,9999999,1):
    recursive(n)

