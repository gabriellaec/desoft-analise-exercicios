def filtra_positivos(lista):
    lista_resposta = []
    i = 0
    while i < len(lista) - 1:
        if lista[i] > 0:
            lista_resposta.append(lista[i])
        i += 1
    return lista_resposta
        
    