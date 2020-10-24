def calcula_norma(lista):
    lista2 = []
    for i in lista:
        lista2.append(abs(i))
    return max(lista2)