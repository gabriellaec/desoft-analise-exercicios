import math
def calcula_distancia_do_projetil(v,y0,θ):
    d=((v**2)/(2*9.8))*(1+((1+((2*9.8*y0)/(v**2)*((math.sin(θ))**2)))))*(math.sin(2*θ))
    return d