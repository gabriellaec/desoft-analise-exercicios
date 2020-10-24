import math

def calcula_distancia_do_projetil(velocidade, theta, altura):
    distancia = ((velocidade ** 2) / 20) * (1 + math.sqrt(1 + ((20 * altura) / ((velocidade ** 2) * math.sin(theta))))) * math.sin(2 * theta)
    return distancia