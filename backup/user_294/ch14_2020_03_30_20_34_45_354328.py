import math
a=((v**2)/(2*9.8))
b=(1+((1+((2*9.8*y0)/(v**2)*((math.sin(θ))**2)))**(1/2)))
c=(math.sin(2*θ))
def calcula_distancia_do_projetil(v,y0,θ):
    d=a*b*c
    return d