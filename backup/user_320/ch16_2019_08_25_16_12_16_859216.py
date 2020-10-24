from math import sqrt
def distancia_euclidiana(x1, y1, x2, y2):
    dist = sqrt(((x1 - y1) ** 2) + ((x2 - y2)** 2))
    return dist