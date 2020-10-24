def calcula_norma(dimensao):
    modulo = []
    for i in dimensao:
        modulo.append(i**2)
    return (sum(modulo))**(1/2)
