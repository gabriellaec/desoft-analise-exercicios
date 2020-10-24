import math

g = 9.8

def calcula_distancia_do_projetil(v, teta, y0):
    v2 = v**2
    numerador = 2*g*y0
    denominador = v2*(math.sin(math.radians(teta)))**2
    raiz = math.sqrt(1 + numerador/denominador)
    fora = math.sin(math.radians(2*teta))
    d = (v2/2*g)*raiz*fora
    return d