import math 

def calcula_distancia_do_projetil(v,x,y):
    d=(v**2)/2*9.8)
    e=(1+(1 + ((2*9.8*y)/(v**2 *(math.sin(x))**2)))**0.5)
    f= math.sin(2*x)
    x=d*e*f
    return x
