import math
def encontra_cateto(h,c1):
    c2 = math.sqrt((h**2)-(c1**2))
    return c2

a = 5
b = 4
c = encontra_cateto(a,b)

print(c)