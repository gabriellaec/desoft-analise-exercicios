# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:49:53 2019

@author: User
"""

somando = True
lista = [0]*101
n = 0
p = 0
valorfinal = 0    

while somando:
    if n<100:
        r = 1/(2**n)
        lista[p]=r
        soma = lista[p]+valorfinal
        valorfinal = soma
        p = p+1
        n = n+1

    else:
        somando = False
        
print (valorfinal)