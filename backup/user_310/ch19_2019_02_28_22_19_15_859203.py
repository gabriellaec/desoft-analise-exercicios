import math

def calcula_distancia_do_projetil(v, teta, y0):
    a= (v**2)/2*10
    b= 2*10*y0
    c= (v**2)*(math.sin(teta))**2
    e=math.sin(2*teta)
    d=a*(1+math.sin(a+(b/c)))*e
    return d