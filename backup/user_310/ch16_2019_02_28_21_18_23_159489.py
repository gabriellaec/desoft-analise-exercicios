import math

def distancia_euclidiana(x1, y1, x2, y2):
    distancia=(x2-x1)**2+(y2-y1)**2
    d= math.sqrt(distancia)
    return d