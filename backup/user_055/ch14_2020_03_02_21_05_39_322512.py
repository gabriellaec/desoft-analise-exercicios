import math

def calcula_distancia_do_projetil(v,θ,y0):
    g = 9.8
    d1 = (v**2)/(2*g)
    d2 = (1 + (1 + (2*g*y0)/((v**2)*(math.sin(θ))**2))**(1/2))
    d3 = math.sin(2*θ)
    return d1*d2*d3  