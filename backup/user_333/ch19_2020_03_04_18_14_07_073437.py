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

lado_a=int(input('a: '))
lado_b=int(input('b: '))
lado_c=int(input('c: '))

print('para a={0}, b={1} e c={2}, {3}'.format(lado_a,lado_b,lado_c,tipo_de_triangulo(lado_a,lado_b,lado_c)))