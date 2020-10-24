import math
def distancia_euclidiana (x1 , y1, x2, y2):
    distancia_x = (x2 - x1)
    distancia_y = (y2 - y1)
    distancia_pontos = ( (distancia_x ** 2) - (distancia_y **2 ))
    return distancia_pontos