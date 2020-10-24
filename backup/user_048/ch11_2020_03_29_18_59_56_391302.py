import math
def distancia_euclidiana(x1,y1,x2,y2):
    a=x1-x2
    b=y1-y2
    d=math.sqrt(a**2+b**2)
    return d
print(distancia_euclidiana(x1, y1, x2, y2))