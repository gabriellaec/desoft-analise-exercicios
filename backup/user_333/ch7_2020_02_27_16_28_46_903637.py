# -*- coding: utf-8 -*-
"""
programa que calcula a área do triângulo informando sua base(b) e altura(h)

@author: Francisco Janela
"""

#função usa a fórmula de cálculo da área do triângulo
def calcula_area_do_triangulo(b,h):
    area_do_triangulo=(b*h)/2
    return area_do_triangulo

#input das medidas da base e da altura para calcular a área
base_b=6
altura_h=23
print('a área do triângulo de base {0} e altura {1} é {2} u.a.'.format(base_b,altura_h,calcula_area_do_triangulo(base_b,altura_h)))