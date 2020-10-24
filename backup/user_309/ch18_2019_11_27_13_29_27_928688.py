cat = 4
hip = 5

def encontra_cateto(cat,hip):
    cateto = ((hip**2) - (cat**2))**(1/2)
    return cateto

print(encontra_cateto(cat,hip))