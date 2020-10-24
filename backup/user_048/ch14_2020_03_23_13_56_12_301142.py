import math
g=9.8
def calcula_distancia_do_projetil(v,o,y):
    a=((v**2)/(2*g))
    b=(2*g*y)/((v**2)*(math.sin(o)**2))
    d=a*(1+math.sqrt(1+b))*math.sin(2*o)
    return d
print(calcula_distancia_do_projetil(v,o,y))                                                           