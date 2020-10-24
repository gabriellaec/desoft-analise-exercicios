import math

def calcula_distancia_do_projetil(v, A, y0):
    D1 = (v**2)/2*9.8
    D2 = 1 + ((2*9.8*y0)/((v**2)*(math.radians(math.sin(A)**2))))
    d= D1 *(1+ math.sqrt(D2)) * math.radians(math.sin(20))
    return d