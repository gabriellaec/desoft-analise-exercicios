import math
def distancia_euclidiana(a,b,c,d):
    return (math.sqrt((b-a)**2)+((d-c)**2))
print(distancia_euclidiana(10,20,40,50))