# -*- coding: utf-8 -*-
"""
programa para encontrar o valor do outro cateto de um triângulo retângulo

@author: Francisco Janela
"""

import math

#função que calcula o cateto desconhecido do triângulo
def encontra_cateto(cat,hip):
    cateto=math.sqrt(hip**2-cat**2)
    return cateto

#input do cateto de da hipotenusa
cateto=5
hipotenusa=13
print('o valor do outro cateto é {0}.'.format(encontra_cateto(cateto,hipotenusa)))