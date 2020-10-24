def encontra_cateto(cateto, hipotenusa):
    encontrado = ((cateto)**2 - (hipotenusa)**2)**1/2
    encontrado*= -1
    return encontrado