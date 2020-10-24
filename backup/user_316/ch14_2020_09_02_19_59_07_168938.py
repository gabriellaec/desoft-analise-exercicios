import math

g = 9.8

def calcula_distancia_do_projetil(v, ang, y0):
    return ((v**2)/2*g)*(1+(math.sqrt(1+((2*g*y0)/(v**2*(math.sin(ang)**2))))))*math.sin(2*ang)

print(calcula_distancia_do_projetil(1, 45, 10))