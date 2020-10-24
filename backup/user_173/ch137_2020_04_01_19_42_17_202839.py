# a frequencia está em rotação por minuto, e pede para retornar em segundo. 

from math import *
def calcula_aceleracao (r,f):
    w = 2*pi*(f/60)
    aceleracao = (w**2)*r
    return aceleracao