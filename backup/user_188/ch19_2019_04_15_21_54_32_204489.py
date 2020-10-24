import math

def calcula_distancia_do_projetil(velocidade, theta, altura):
    g = 9.8
    
    pre = 2*g*altura / (velocidade**2 * (math.sin(theta))**2)
    parte = math.sqrt(1 + preparte)
    return velocidade ** 2 / (2*g) * (1+ parte) * math.sin(2*theta)