import math
def calcula_distancia_do_projetil(v,θ,y0):
    a=((v**2)/(2*9.8))
    b=1
    d=(1+(2*9.8*y0)/((v**2)*((math.sin(θ))**2))**(1/2))
    c=math.sin(2*θ)
    y=a*(b+d)*c
    return y
