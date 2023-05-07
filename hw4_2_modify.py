# -*- coding: utf-8 -*-
"""

第二小題

因為電腦計算到n=50完，計算n=60的時候跑了很久，所以假設n=60時，
使用recursion會發生crash，改使用Dynamic Programming的話並不會發生crash，
並且也測試n=59、n=61使用Dynamic Programming會不會發生crash

"""


# Fibonacci Series using Dynamic Programming
def dynamic_programming(n):
 
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        
    return f[n]

ans_59 = dynamic_programming(60-1)
ans_60 = dynamic_programming(60)
ans_61 = dynamic_programming(60+1)
            