def equaliza_imagem(lista, K):
    lista_nova = []
    i = 0
    X = len(lista)
    while i <= (X-1):
        if (lista[i]*K) >= 255:
            lista_nova.append(255)
        else:
            lista_nova.append(lista[i]*K)
        i += 1
    return lista_nova