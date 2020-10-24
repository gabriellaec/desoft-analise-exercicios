#coding: utf-8
from math import sin
from math import sqrt
def  calcula_distancia_do_projetil(v,θ,y0):
    g = 9.8
    a = v**2 / 2*g
    b = 1 + 2*g*y0
    c = v**2 * (sin(θ))**2
    distancia = a * ( 1 + math.sqrt(b/c)) * sin(2*θ)
    return distancia