# -*- coding: utf-8 -*-
"""
calcula a distância alcançada por um projétil

@author: Francisco Janela
"""
import math

#define a constante gravitacional
g=9.8

#função que usa a fórmula para calcular a distância do projétil
def calcula_distancia_do_projetil(v,teta,y0):
    seno=math.sin(2*teta)
    raiz_quociente=(v**2)*(math.sin(teta)**2)
    raiz_numerador=2*g*y0
    raiz=math.sqrt(1+(raiz_numerador/raiz_quociente))
    distancia=((v**2)/(2*g))*(1+raiz)*seno
    return distancia

#input das variáveis para o cálculo da distância
velocidade=30
angulo_θ=45
altura_inicial=2
print('a distância percorrida pelo projétil é {0}'.format(calcula_distancia_do_projetil(velocidade,angulo_θ,altura_inicial)))