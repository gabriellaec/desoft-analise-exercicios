# -*- coding: utf-8 -*-
"""
programa que calcula a gaussiana de 3 inputs de valores reais

@autor: Franciso Janela
"""
#importar a biblioteca math para adquirir funções e contante matematicas
import math

#função que calcula a formula gaussiana para quaisquer 3 números reais
def calcula_gaussiana(x,mi,sigma):
    exponencial_neperiano=(-0.5)*((x-mi)/sigma)**2
    gaussiana=(1/(sigma*math.sqrt(2*math.pi)))*math.e**exponencial_neperiano
    return gaussiana

#introduzir os 3 valores reais
valor_de_x=3.5
valor_de_mi=6.89
valor_de_sigma=0.2
print('a gaussiana de x={0}, mi={1} e sigma={2} é: {3}.'.format(valor_de_x,valor_de_mi,valor_de_sigma,calcula_gaussiana(valor_de_x,valor_de_mi,valor_de_sigma)))
