import math
g = 9.8
def  calcula_distancia_do_projetil(v,a,h):
    a = ((v**2)/(2*g))
    b = math.sqrt(1 + ((2*g*h)/((v**2)*(math.sin(a)**2))))
    c = math.sin(2*a)
    d = a*(1+b)*c
    return d