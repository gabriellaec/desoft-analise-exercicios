import math
def distancia_euclidiana(xo, yo, xi, yi):
    distancia = math.sqrt(((xo - xi) ** 2) + ((yo - yi) **2))
    return distancia