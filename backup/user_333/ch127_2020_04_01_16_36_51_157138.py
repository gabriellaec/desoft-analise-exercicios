import math

def calcula_elongacao(A,finicial,vangular,t):
    parenteses_em_rad=math.radians(finicial+vangular*t)
    x=A*math.cos(parenteses_em_rad)
    return x
    