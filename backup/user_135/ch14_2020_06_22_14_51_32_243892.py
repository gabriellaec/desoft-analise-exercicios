import math

def calcula_distancia_do_projetil(v, teta, y0):
    g = 9.8
    v2 = v**2
    numerador = 2*g*y0
    denominador = v2*(math.sin(teta))**2
    raiz = 1 + math.sqrt(1 + numerador/denominador)
    fora = math.sin(2*teta)
    d = (v2/2*g)*raiz*fora
    return d