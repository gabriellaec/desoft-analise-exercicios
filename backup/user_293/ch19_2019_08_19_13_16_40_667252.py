import math
def  calcula_distancia_do_projetil(v,a,h):
    a = ((v**2)/(2*9.8))
    b = math.sqrt(1 + ((2*9.8*h)/((v**2)*(math.sin(a)**2))))
    c = math.sin(2*a)
    d = a*b*c
    return d