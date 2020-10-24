import math
cateto = float(input('Qual a medida do cateto?:'))
hipotenusa = float(input('Qual a medida da hipotenusa?:'))

def encontra_cateto(cateto,hipotenusa):
    ca = ((hipotenusa*hipotenusa) - (cateto*cateto))**(1/2)
    return ca

print(encontra_cateto)


    