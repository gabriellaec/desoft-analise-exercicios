# -*- coding: utf-8 -*-
"""
programa que encontra a raíz de uma função do primeiro grau

@author: Francisco Janela
"""

#cálculo da raíz de uma função do primeiro grau defenida por 0=ax+b
def resolve_equacao_1o_grau(a,b):
    x=(-1*b)/a
    return x

#input do coeficiente angular(a) e do coeficiente linear(b)
a=4
b=-60
print('a raíz da equação é {0}.'.format(resolve_equacao_1o_grau(a,b)))