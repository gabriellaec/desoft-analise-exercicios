# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 08:08:33 2019

@author: carol
"""
def eh_primo (n):
    if n==2:
        return True
    if n==0 or n==1:
        return False
    i=2
    while  i<n:
        if n % i == 0:
        	return False 
        i = i+1
    return True 

def imprime_primos (x):
    i=0
    j=0
    while i<x:
        if eh_primo(j) == True:
            print(j)
            i=i+1
        j = j+1  

