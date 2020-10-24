from math import sqrt

def encontra_cateto(cateto, hipotenusa):
    outro_cateto = sqrt((hipotenusa ** 2) - (cateto ** 2))
    return outro_cateto