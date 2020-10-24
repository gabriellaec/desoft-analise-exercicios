import math
def calcula_distancia_do_projetil(v,alpha,y0):
    g = 9.8
    d1 = v**2/2*g
    d2 = 2*g*y0
    d3 = (v**2)*(math.sin(alpha))**2
    d4 = math.sin(2*alpha)
    d = d1*( 1 + (1 + (d2/d3)**(0.5)))*d4
    return d
    