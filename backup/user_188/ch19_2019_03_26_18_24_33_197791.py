import math

def calcula_distancia_do_projetil(velocidade, theta, altura):
    distancia = ((velocidade ** 2) / 2*9.8) * (1 + math.sqrt(1 + ((2*9.8 * altura) / ((velocidade ** 2) * (math.sin(theta) ** 2))))) * math.sin(2 * theta)
    return distancia