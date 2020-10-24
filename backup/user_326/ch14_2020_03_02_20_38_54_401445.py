import math
g = 9.8
def calcula_distancia_do_projetil(velocidade, angulo, altura):
    distancia = ((velocidade**2) / 2*g) *(1 + math.sqrt(1 +2*g*altura/((velocidade**2)*(math.sin(angulo)**2))))*math.sin(2*angulo)
    return distancia