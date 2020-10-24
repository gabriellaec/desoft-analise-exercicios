def encontra_cateto(cateto,hipotenusa):
    c = ((hipotenusa**2) - (cateto**2))**0.5
    return c
r=5
s=3
d= encontra_cateto(r,s)

print(d)