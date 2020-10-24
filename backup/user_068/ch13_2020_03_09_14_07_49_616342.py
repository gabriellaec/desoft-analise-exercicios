def encontra_cateto(cateto, hipotenusa):
    a = (hipotenusa**2 - cateto**2)**(1/2)
    return a
b=4
c=5
r = encontra_cateto(b, c)
print(r)