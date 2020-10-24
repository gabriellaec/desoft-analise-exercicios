from math import sqrt
def distancia_euclidiana(x1,y1,x2,y2):
    d1 = (x2-x1)**2
    d2 = (y2-y1)**2
    d = sqrt(d1 + d2)
    return d