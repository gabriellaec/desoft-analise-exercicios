import math

def calcula_distancia_do_projetil(v, θ, y0, g):
    parte1 = (v**2)/2*g
    parte2 = (1+(1+(2*g*y0)/(v**2*(math.sin(θ))**2))**(1/2))
    parte3 = math.sin(2*θ)
    return parte1*parte2*parte3