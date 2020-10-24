# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:12:40 2020

@author: franc
"""

def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'equilátero'
    elif a==b or a==c or b==c:
        if a!=b:
            return 'isósceles'
        elif a!=c:
            return 'isósceles'
        else:
            return 'isósceles'
    else:
        return 'escaleno'


print(classifica_triangulo(4,5,6))