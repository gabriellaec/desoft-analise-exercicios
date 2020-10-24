import math
g=9.8
def calcula_distancia_do_projetil(v,teta,y0):
    d=(v**2)/2*g*((1+(1+2*y0*g/(v**2)*(math.sin(math.radians(teta))**2))*2*math.sin(math.radians(teta))*math.cos(math.radians(teta))))
    return d