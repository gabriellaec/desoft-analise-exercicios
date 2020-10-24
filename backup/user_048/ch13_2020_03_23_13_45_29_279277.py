import math
def encontra_cateto(c2,h):
    c1=math.sqrt((h**2)-(c2**2))
    return c1
print(encontra_cateto(4,5))