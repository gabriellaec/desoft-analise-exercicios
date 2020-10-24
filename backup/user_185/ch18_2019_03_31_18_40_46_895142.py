import math
def encontra_cateto(cateto_1, hipotenusa):
    cateto_2 = math.sqrt((hipotenusa**2) - (cateto_1**2))
    return cateto_2