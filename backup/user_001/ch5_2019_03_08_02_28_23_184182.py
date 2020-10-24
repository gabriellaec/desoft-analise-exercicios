# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:51:38 2019

@author: Admin
"""

def maior_primo_menor_que(n):
    if n<0:
        return -1
    elif n<2:
        return 0
    elif n==2:
        return 1
    else:
        for r in range(2, n):
            if n%r == 0:
                return 0
            
    return 1


n=4
print(maior_primo_menor_que(n))
