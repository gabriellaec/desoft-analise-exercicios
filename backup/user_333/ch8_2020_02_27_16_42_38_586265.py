# -*- coding: utf-8 -*-
"""
programa calcula a posição final do objeto no MRU no SI

@author: Fracisco Janela
"""

#funcao calcula a posição final através da fórmula de distância pelo tempo do MRU
def calcula_posicao(t,s0,v):
    s=s0+v*t
    return s

#input dos dados utilizados para calcular a posição final:tempo, posição inicial e velocidade
tempo_em_segundos=30
posição_inicial_em_metros=150
velocidade_em_metros_por_segundo=20
print('a posição final do objeto é {0}m.'.format(calcula_posicao(tempo_em_segundos,posição_inicial_em_metros,velocidade_em_metros_por_segundo)))