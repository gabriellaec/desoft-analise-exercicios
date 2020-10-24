import math

def distancia_euclidiana(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) **2
    raiz = math.sqrt(dist)
    return raiz