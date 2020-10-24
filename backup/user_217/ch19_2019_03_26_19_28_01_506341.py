import math
g=9.8
def calcula_distancia_do_projetil(v,an,yo):
    d= (v**2)/(2*g)*(1+(1+(2*g*yo)/(v**2)*(math.sin(an)**2))**0.5)*math.sin(2*an)
    return d