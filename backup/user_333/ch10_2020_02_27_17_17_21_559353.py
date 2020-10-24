# -*- coding: utf-8 -*-
"""
programa para calcular o volume de uma pizza

@author: Francisco Janela
"""
import math

#função que calcula o volume de uma pizza, considerando-a um cilindro
def volume_da_pizza(z,a):
    area_superficial=math.pi*z**2
    volume=area_superficial*a
    return volume

#input do raio e da altura da pizza
raio_da_pizza=15
altura_da_pizza=1.5
print('o volume da pizza é {0}.'.format(volume_da_pizza(raio_da_pizza,altura_da_pizza)))