def encontra_maximo(matriz):
    lista_0 = matriz[0]
    lista_1 = matriz[1]
    lista_2 = matriz[2]
    # Parâmetro de valor máximo
    maximo = abs(lista_0[0])
    for lista in matriz:
        # Roda elementos de cada lista e compara com o máximo
        for numero in lista:
            if abs(numero) > maximo:
                maximo = abs(numero)
    return maximo