import math
g=9.8
def calcula_distancia_do_projetil(v,θ,y0):
    d =((v**2/2*g))
    a=(1+((2*g*y0)/(v**2)*(math.sin(θ)**2))**(1/2)
    y=(d*a)*math.sin(2*θ)
    return y