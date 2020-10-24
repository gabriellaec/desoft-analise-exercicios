import math

def distancia_euclidiana(x1, y1, x2, y2):
    return math.sqrt( ((x2 - x1)**2) + ((y2-y1)**2) )

print(distancia_euclidiana(1, 2, 5, 6))