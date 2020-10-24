from math import sqrt

def distancia_euclidiana (x1, x2, y1, y2):
    distancia = sqrt(((x1-y1)**2))+((x2-y2)**2)
    return distancia