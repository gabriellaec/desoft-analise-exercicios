import math

def calcula_distancia_do_projetil(v, teta, y0):
    a=(v**2)*((math.sin(teta*2))**2)
    b=2*9.8*y0
    c=(v**2)/(2*9.8)
    d=math.sin(2*teta)
    e=math.sqrt(1+(b/a))
    gaussiana=c*(1+(e))*d
    return gaussiana