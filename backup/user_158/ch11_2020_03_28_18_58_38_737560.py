import math
def distancia_euclidiana(x1,y1,x2,y2):
    De = math.sqrt((x2-x1)+(y2-y1))
    return De

print(distancia_euclidiana(5,5,5,5))