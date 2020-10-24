def equaliza_imagem(lista, k):
    nova_lista = [0]*len(lista)

    for posicao in range(len(lista)):
        nova_lista[posicao] = lista[posicao] * k

        if nova_lista[posicao] > 255:
            nova_lista[posicao] = 255

    return nova_lista