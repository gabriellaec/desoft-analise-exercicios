import math

def encontra_cateto(ctt,h):
    cateto= h**2 - ctt**2
    return math.sqrt(cateto)

print(encontra_cateto(3, 5))