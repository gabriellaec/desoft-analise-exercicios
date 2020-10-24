import math
def distancia_euclidiana(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(distancia_euclidiana(2,3,4,4))