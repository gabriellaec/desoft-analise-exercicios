import math
def distancia_euclidiana(x1,y1,x2,y2):
    d = math.sqrt(((y2 - y1)**2) + ((x2 - x1)**2))
    return d
x1 = 2
x2 = 5
y1 = 7
y2 = 11
c = distancia_euclidiana(x1,y1,x2,y2)

print(c)