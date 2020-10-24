def encontra_cateto(cateto,hipotenusa):
    c = ((cateto**2) - (hipotenusa**2))**0.5
    return c
cateto=5
hipotenusa=3
d= encontra_cateto(cateto,hipotenusa)

print(d)