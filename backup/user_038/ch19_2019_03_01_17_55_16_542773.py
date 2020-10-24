import math
def calcula_distancia_do_projetil(velocidade, angulo, altura):
    distancia = (velocidade**2/2*9.8)*(1 + (1 + 2*9.8*altura/velocidade**2*math.sin(angulo)**2)**(1/2))*math.sin(2*angulo)
    return distancia