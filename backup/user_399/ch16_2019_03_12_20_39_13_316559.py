import math
def distancia_euclidiana(x1,x2,y1,y2):
    dx=(x1-x2)**2
    dy=(y1-y2)**2
    d=math.sqrt(dx+dy)
    return d