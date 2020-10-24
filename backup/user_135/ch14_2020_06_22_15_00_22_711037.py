import math

def calcula_distancia_do_projetil(v, angulo, y0):
    g = 9.8
    fora1 = (v**2)/2*g
    raiz = math.sqrt(1 + (2*g*y0/v**2*math.sin(angulo)**2)
    fora2 = math.sin(2*angulo)
    d = fora1*(1+raiz)*fora2
    return d