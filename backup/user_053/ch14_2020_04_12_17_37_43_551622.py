import math

def calcula_distancia_do_projetil(v, teta, y_0):
    a = (v**2/(2*9.8))*math.sin(2*teta)
    b = (2*9.8*y_0)/((v**2)*(math.sin(teta))**2)
    c = math.sqrt(1 + b)
    d = 1 + c
    distancia = a*d
    return distancia