import math

def calcula_distancia_do_projetil(v,teta,y0):
    g = 9.8
    rad = math.radians(teta)
    a = 2*g*y0
    o = (v**2)*(math.sin(rad)**2)
    dist = (v**2)/(2*g)*((1 + a/o)**1/2)*math.sin(2*rad)
    return dist