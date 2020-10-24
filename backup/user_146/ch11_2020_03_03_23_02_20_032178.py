import math
def distancia_euclidiana(b,a,d,c):
    return (math.sqrt(((b-a)**2)+((d-c)**2)))
print(distancia_euclidiana(1,1,1,4))