# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:22:54 2019

@author: User
"""

def eh_primo(x):
    if x==0:
        return False
    elif x==1:
        return False
    else:
        d = 3
        while d<=x:
            if x == 2:
                return True
            else:
                if x==d:
                    return True
                if x%d == 0:
                    return False
                else:
                    d = d+2
                
            
numero = int(input("Descubra se um número é primo ou não: "))
print(eh_primo(numero))