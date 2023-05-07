# -*- coding: utf-8 -*-
"""

第一小題

因為電腦計算到n=50完，計算n=60的時候跑了很久，所以後面的數字使用"標程某個大值"

"""
import matplotlib.pyplot as plt
import numpy as np

n_list = list(range(10, 100+10, 10))

execution_time_r_list = [0.0,
                         0.0019948482513427731,
                         0.24135613441467285,
                         29.404333114624023,
                         3571.043809890747, #前面五筆資料平均差123倍
                         3571.043809890747*123,
                         3571.043809890747*123*123,
                         3571.043809890747*123*123*123,
                         3571.043809890747*123*123*123*123,
                         3571.043809890747*123*123*123*123*123]

execution_time_dp_list = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,]




plt.plot(np.array(n_list), np.array(execution_time_dp_list), label='dynamic programming')
plt.plot(np.array(n_list), np.array(execution_time_r_list), label='recursive')

plt.xlabel("n")
plt.ylabel("execution time")
plt.legend()
plt.show()