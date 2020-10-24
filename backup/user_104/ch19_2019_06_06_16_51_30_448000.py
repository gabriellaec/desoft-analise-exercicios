import math
def calcula_distancia_do_projetil(v, teta, y0):
    g = 9.8
    a = (v**2)/(2*g)
    b = 2*g*y0
    c = (v**2)*(math.sin(teta)**2)
    d =math.sqrt(1+(b/c))
    e = math.sin(2*teta)
    resultado = a*(1+d)*e
    return resultado