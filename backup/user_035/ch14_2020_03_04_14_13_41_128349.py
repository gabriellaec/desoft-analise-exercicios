import math

g = 9.8

def calcula_distancia_do_projeto(v,teta,altura_inicial):
    a = (v**2/2*g)*(1+(1+2*g*altura_inicial)/(v**2*((math.sin(teta))**2))//2)*math.sin(2*teta)
    return a