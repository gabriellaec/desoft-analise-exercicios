import math
def distancia_euclidiana(x1, y1, x2, y2):
    dist = math.sqrt((x2-x1)**2 * (y2-y1)**2)
    return dist
print (distancia_euclidiana(1,2,3,4))