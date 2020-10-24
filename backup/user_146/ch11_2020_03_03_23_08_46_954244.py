import math
def distancia_euclidiana(a,b,c,d):
    return (math.sqrt(((c-a)**2)+((d-b)**2)))
print(distancia_euclidiana(1,1,1,4))