from math import sqrt
def encontra_cateto(c1,h):
    #h**2 = c1**2 + c2**2
    #c2**2 = h**2 - c1**2
    c2 = sqrt((h**2)-(c1**2))
    return c2