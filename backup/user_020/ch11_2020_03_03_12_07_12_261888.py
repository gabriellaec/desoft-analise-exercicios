# Programa que calcula a distância entre dois pontos no plano cartesiano
import math
def distancia_euclidiana(x1,y1,x2,y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d
print(distancia_euclidiana(1,2,3,4))