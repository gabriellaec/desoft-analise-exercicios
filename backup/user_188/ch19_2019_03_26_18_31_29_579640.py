def calcula_distancia_do_projetil(velocidade, theta, altura):
    import math
    a =(velocidade ** 2)/(2 * 9.8)
    b =(1 +  (2 * 9.8 * altura))/((velocidade ** 2) * (math.sin(theta) ** 2))
    c = 1 + math.sqrt(b)
    d = math.sin(2 * theta)
    distancia = a * c * d
    return distancia