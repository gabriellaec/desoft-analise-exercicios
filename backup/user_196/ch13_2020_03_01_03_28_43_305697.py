from math import sqrt
def encontra_cateto (cateto, hipotenusa):
    catetu = sqrt (cateto**2 + hipotenusa**2)
    return catetu 

a=5
b=7
cat = encontra_cateto(a,b)
print (cat)