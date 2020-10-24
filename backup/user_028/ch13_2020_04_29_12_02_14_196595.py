import math
def encontra_cateto(hip,cat):
    cateto1= (hip**2) - (cat**2)
    cateto=math.sqrt(cateto1)
    return cateto
print(encontra_cateto)