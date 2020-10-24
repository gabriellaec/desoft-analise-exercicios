import math 
def calcula_distancia_do_projetil(v, a, y):
    g = 9.8
    d = v**2/(2*g)*(1+(1+2*g*y/(v**2)*((math.sin(a))**2)**1/2))*math.sin(2*a)