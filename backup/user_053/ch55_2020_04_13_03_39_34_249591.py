def encontra_maximo(matriz):
    lista0 = matriz[0]
    lista1 = matriz[1]
    lista2 = matriz[2]

    maximo = abs(lista0[0])
    for lista in matriz:
        for numero in lista:
            if abs(numero) > maximo:
                maximo = abs(numero)
    return maximo