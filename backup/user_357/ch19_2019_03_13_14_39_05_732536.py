import math
def calcua_distancia_projetil(angulo,velocidade,altura):
    g = 9.8
    a = 2*g*altura
    b = velocidade**2 * (math.sin(angulo))**2
    c = math.sin(2*angulo)
    d = velocidade**2 / (2*g)
    return d * (1 + (1 + a/b)**(1/2))*c
