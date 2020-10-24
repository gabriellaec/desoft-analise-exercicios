import math
def encontra_cateto(cateto_a, hipotenusa):
    cateto_b=math.sqrt(hipotenusa**2-cateto_a**2)
    return cateto_b
