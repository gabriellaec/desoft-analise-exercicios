# -*- coding: utf-8 -*-
"""
programa que calcula a distância de dois pontos no plano cartesiano

@author: Francisco Janela
"""

import math #obter função raíz quadrada

#função que calcula a distância euclidiana entre dois pontos do plano cartesiano
def distancia_euclidiana(x1,y1,x2,y2):
    diferenca_x=x2-x1
    diferenca_y=y2-y1
    distancia=math.sqrt(diferenca_x**2+diferenca_y**2)
    return distancia

#input dos pares ordenados dos pontos para cálculo da distÂncia entre eles
ponto_1=(7,8)
ponto_2=(15,16)
print('{0}'.format(distancia_euclidiana(ponto_1[0],ponto_1[1],ponto_2[0],ponto_2[1])))