from math import sqrt
def encontra_cateto(h, c1):
    a = sqrt(h**2 - c1**2)
    return a

print(encontra_cateto(5, 4))