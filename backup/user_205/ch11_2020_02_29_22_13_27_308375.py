import math
def distancia_euclidiana (x1,y1,x2,y2):
    Distancia = math.sqrt ((y2-y1)**2 + (x2-x1)**2)
    return Distancia
print (distancia_euclidiana (5,4,3,2))