def encontra_maximo(matriz):
    lista_maior_linha = []
    for lista in matriz:
        lista_absoluto = []
        for numero in lista:
            lista.absoluto.append(abs(numero))
        lista_maior_linha.append(max(lista_absoluto))
    return max(lista_maior_linha)