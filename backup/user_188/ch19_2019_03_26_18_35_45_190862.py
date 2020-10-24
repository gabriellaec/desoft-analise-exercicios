import math

def calcula_distancia_do_projetil(velocidade, theta, altura):
    d1 = ((velocidade ** 2)/(2 * 9.8))
    d2 = (1 + math.sqrt(1 + ((2 * 9.8 * velocidade)/((velocidade ** 2)*(math.sin(theta)**2)))))
    d3 = math.sin(2 * theta)
    distancia = d1 * d2 * d3
    return distancia