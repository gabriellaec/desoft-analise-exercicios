import math

def calcula_distancia_do_projetil(v,angulo, y0):
    g = 9.8
    d = (v**2/2*g)*(1+math.sqrt(1+(2*g*y0/(v**2*(math.sin(angulo))**2))))*math.sin(2*angulo)
    return d

print(calcula_distancia_do_projetil(5, 30, 0))