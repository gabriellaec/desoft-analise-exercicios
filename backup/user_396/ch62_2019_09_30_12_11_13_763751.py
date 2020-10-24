def filtra_positivos(lista):
    lista_resposta = list()
    i = 0
    while i < len(lista) - 1:
        if lista[i] > 0:
            lista_resposta.append(lista[i])
            return lista_resposta
        i += 1
    