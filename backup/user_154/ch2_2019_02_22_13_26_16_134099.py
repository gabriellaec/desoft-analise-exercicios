def calcula_velocidade_media(distancia, horas):
    if (distancia < 1 or horas < 1):
        return 0
    if (distancia == horas):
        return 1
    if (distancia > 1000):
        return distancia//horas
    return disntancia//horas