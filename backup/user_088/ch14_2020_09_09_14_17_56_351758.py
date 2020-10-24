import math
def calcula_distancia_do_projetil(v,T,yo):
    g=9.8
    d1=(v**2/2*9.8)
    d2=1+(1+(2*9.8*yo/(v**2)*math.sin(T)**2))**1/2
    d3=math.sin(2*T)
    return d1*d2*d3