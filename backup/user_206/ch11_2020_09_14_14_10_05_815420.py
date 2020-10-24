import math
def distancia_euclidiana(x1, y1, x2, y2):
    distancia = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
    return(distancia)