# -*- coding: utf-8 -*-
"""

第一小題

"""
import matplotlib.pyplot as plt
import numpy as np
import time

n_list = list(range(10, 100+10, 10))

methods = ['recursive', 'dynamic_programming']

execution_time_r_list = []
execution_time_dp_list = []

# Fibonacci series using recursion
def recursive(n):
    
    if n <= 1:
        return n

    return recursive(n-1) + recursive(n-2)
    

# Fibonacci Series using Dynamic Programming
def dynamic_programming(n):
 
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        
    return f[n]


for n in n_list:
    for method in methods:
        if method == 'dynamic_programming':
            start = time.time()
            ans = dynamic_programming(n)
            end = time.time()
            execution_time_dp_list.append(end-start)
            print('dp n={} time={}'.format(n,end-start))
          
        else :
            start = time.time()
            ans = recursive(n)
            end = time.time()
            execution_time_r_list.append(end-start)
            print('r n={} time={}'.format(n,end-start))
        


plt.plot(np.array(n_list), np.array(execution_time_dp_list), label='dynamic programming')
plt.plot(np.array(n_list), np.array(execution_time_r_list), label='recursive')

plt.xlabel("n")
plt.ylabel("execution time")
plt.legend()
plt.show()