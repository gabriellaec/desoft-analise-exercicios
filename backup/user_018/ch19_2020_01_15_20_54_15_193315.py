from math import sqrt,sin
g = 9.8
def calcula_distancia_do_projetil (g,v,teta,yo):
    a = 1 + sqrt((1+((2*g*yo)/((v**2)/sin(teta)**2)))
    d = ((v**2)/2*g)*a*(sin(2*teta)) 
    return d