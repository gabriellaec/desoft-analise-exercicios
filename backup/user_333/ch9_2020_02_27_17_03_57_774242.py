# -*- coding: utf-8 -*-
"""
programa calcula  volume da esfera em função de seu raio

@author: Francisco Janela
"""
import math

#função utiliza a fórmula para cálculo do volume de uma esfera
def calcula_volume_da_esfera(R):
    volume=(4/3)*math.pi*R**3
    return volume

#input do raio da esfera
raio_da_esfera=7
print('o volume da esfera de raio {0} é {1}.'.format(raio_da_esfera,calcula_volume_da_esfera(raio_da_esfera)))