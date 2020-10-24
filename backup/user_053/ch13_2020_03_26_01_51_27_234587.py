from math import sqrt

def encontra_cateto(cat,hip):
    cateto=sqrt(hip**2-cat**2)
    return cateto

a=5
b=4
c=encontra_cateto(4,5)

print(c)