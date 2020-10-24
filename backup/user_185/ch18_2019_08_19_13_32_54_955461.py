import math
math.sqrt = raiz
def encontra_cateto (cateto1, cateto2, hipotenusa):
    cateto1_quadrado = cateto1 ** 2
    hipotenusa_quadrado = hipotenusa ** 2
    cateto2 = raiz ( cateto1_quadrado + hipotenusa)
    return cateto2
    