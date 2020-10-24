hipotenusa = 5
cateto_conhecido = 4

def encontra_cateto(hipotenusa, cateto_conhecido):
    cateto_desconhecido = ((hipotenusa**2) - (cateto_conhecido**2))**(1/2)
    return cateto_desconhecido

print(encontra_cateto(hipotenusa, cateto_conhecido))