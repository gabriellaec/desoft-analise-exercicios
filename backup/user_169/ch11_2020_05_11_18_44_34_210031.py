import math
def distancia_euclidiana(x1,y1,x2,y2):
    dx=x1-x2
    dy=y1-y2
    d=(pow(dx,2)-pow(dy,2))
    return math.sqrt(d)
