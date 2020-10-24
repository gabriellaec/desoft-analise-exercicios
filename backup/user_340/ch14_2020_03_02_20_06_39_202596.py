import math
g=9.8
def calcula_distancia_do_projetil(v,x,y0):
    a=((v**2)/(2*g))
    b= 1 + (2*g*y0)/((v**2)*(math.sin(x))**2)
    d = a*(1+b)*math.sin(2*x)
    return d

