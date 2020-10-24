import math

def calcula_distancia_do_projetil(velocidade, theta, altura):
    g = 9.8
    
    d1 = ((velocidade ** 2)/(2 * g))
    pred2 = 2 * g * velocidade / (velocidade**2 * math.sin(theta)**2)
    d2 = math.sqrt(1 + pred2)
    d3 = math.sin(2 * theta)
    distancia = d1 * (1 + d2) * d3
    return distancia