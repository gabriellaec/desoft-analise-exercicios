import math

def calcula_distancia_do_projetil(v, A, y0):
    g=9.8
    D1 = (v**2)/2*g
    D2 = 1+((2*g*y0)/((v**2)*math.sin(A)**2))
    d= D1 * math.sqrt(D2) * math.sin(20)
    return d