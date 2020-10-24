def calcula_norma(lista):
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    return (sum(lista2))**0.5