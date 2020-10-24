import math
def calcula_distancia_do_projeto(velocidade, angulo, altura, gravidade):
    distancia = velocidade**2/(2*gravidade)*(1 + (1 + 2*gravidade*altura/velocidade**
                              2*math.sin(angulo)**2)**(1/2))*math.sin(2*angulo)
    return distancia