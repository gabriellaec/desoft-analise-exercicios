
import math as m

def calcula_distancia_do_projetil(v, teta0, y0):
    g = 9.8

    a = (v**2)/2*g
    b = 1 + m.sqrt(1 + (2*g*y0/v**2*(m.sin(teta0)**2)))
    c = m.sin(2*teta0)

    Distancia = a * b * c