def encontra_cateto(cateto2, hipotenusa):
    cateto1 = ((hipotenusa**2) - (cateto2**2))**(1/2)
    return cateto1
a = 6
b = 10
c = encontra_cateto(a, b);
print(c);