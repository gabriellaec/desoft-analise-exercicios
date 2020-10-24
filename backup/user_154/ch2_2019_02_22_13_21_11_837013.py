def calcula_velocidade_media(distancia, horas):
    if (distancia < 0):
        return 0
    if (distancia == horas):
        return 1
    if (distancia > 1000):
        return distancia/horas
    return disntancia/horas