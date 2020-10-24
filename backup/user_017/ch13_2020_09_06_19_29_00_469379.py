def encontra_cateto(cateto,hipotenusa):
    c = ((cateto**2) - (hipotenusa**2))**0.5
    return c
r=5
s=3
d= encontra_cateto(r,s)

print(d)