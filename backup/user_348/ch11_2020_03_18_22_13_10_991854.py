import math
def distancia_euclidiana(x1, x2, y1, y2):
    a = (x2 - x1)**2
    b = (y2 - y1)**2
    c = a + b
    d = math.sqrt(c)
    return d