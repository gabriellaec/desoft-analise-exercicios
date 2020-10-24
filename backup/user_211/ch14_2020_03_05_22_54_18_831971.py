import math
def calcula_distancia_do_projetil(v,t,a):
    p1=((v**2)/(2*9.8))
    p2=(1+(math.sqrt(1+(2*9.8*a)/(v**2(math.sin(t))**2))))
    p3=sin(2*t)
    dist=p1*p2*p3
    return dist