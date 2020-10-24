import math
g=9.8
def calcula_distancia_do_projetil(v,o,yo):
    s=v**2/2*g(1+(1+(2*g*yo)/(v**2*(math.sin(o))**2)*math.sin(2*o)))
    return s
