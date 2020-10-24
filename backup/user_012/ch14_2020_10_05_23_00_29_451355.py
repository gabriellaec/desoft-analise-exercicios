import math
g=9.8
def calcula_distancia_do_projetil(v,t,y):
    a= v**2/2*g
    b= 1+(1+2*g*y/(v**2)*(math.sin(t))**2)**0.5
    c= math.sin(2*t)
    return a*b*c

