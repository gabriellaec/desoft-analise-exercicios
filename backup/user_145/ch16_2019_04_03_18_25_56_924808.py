from math import sqrt
def distancia_euclidiana(x1,y1,x2,y2):
    a = (x2-x1)**2
    b = (y2-y1)**2
    distancia = sqrt(a+b)
    return distancia