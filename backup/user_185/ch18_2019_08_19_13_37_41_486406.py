import math
raiz = math.sqrt
def encontra_cateto (cateto1, hipotenusa):
    cateto1_quadrado = cateto1 ** 2
    hipotenusa_quadrado = hipotenusa ** 2
    cateto2 = raiz( hipotenusa_quadrado - cateto1_quadrado )
    return cateto2