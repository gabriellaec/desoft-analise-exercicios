import math
def encontra_cateto(a,b):
    c = math.sqrt(a**2 - b**2)
    return c

a = 5
b = 4
resultado = encontra_cateto(a,b)

print(resultado)