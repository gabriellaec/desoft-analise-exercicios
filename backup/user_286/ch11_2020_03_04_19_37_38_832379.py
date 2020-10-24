import math

def distancia_euclidiana (x1, y1, x2, y2):
    distx = math.fabs(x1 - x2)
    disty = math.fabs(y1 - y2)
    dist = math.sqrt(distx**2 + disty**2)
    return dist