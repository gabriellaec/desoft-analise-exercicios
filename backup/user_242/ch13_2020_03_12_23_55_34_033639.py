import math
co = float(input('Qual a medida do cateto? '))
hip = float(input('Qual a medida da hipotenusa?'))

def encontra_cateto(co,hip):
    ca = ((hip**2) - (co**2))**1/2
    return ca

print(encontra_cateto)


    