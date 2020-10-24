import math

def calcula_distancia_do_projetil(v,o,yo):
    g=9.8
    p1=v**2/(2*g)
    p3=math.sin(2*o)
    p4=1+(1+2*g*yo/(v**2*(math.sin(o)**2)))**0.5
    s=p1*p4*p3
    return s
