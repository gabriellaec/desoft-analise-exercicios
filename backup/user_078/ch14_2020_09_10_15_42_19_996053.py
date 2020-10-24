
import math as m

g = 9.8
def calcula_distancia_do_projetil(g, v, teta0, y0):

    a = (v**2)/2*g
    b = 1 + m.sqrt(1 + (2*g*y0/v**2*(m.sin(teta0)**2)))
    c = m.sin(2*teta0)

    Distancia = a * b * c