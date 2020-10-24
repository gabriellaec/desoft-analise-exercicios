import math

def calcula_distancia_do_projetil(v,o,yo):
    g=9.8
    p1=v**2/(2*g)
    p2=(math.sin(o))**2
    p3=math.sin(2*o)
    p4=(1+(2*g*yo))
    p5=(v**2)
    s=p1*(1+p4/(p5*p2)**0.5*p3
    return s
