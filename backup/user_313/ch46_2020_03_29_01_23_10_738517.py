def numero_no_indice(lista):
    dados = lista
    c = len(dados)
    contador = 0
    novalista = []*c

    while c != contador:
        if lista[contador] == contador:

            novalista.append(lista[contador])
            contador = contador + 1
        else:
            contador = contador + 1
    return novalista