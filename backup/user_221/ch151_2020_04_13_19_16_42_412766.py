def classifica_lista(lista):
    i = 1
    if len(lista) < 2:
        return 'nenhum'
    while i < len(lista):
        if lista[i] > lista[i-1]:
            return 'crescente'
        i += 1
        if lista[i] < lista[i-1]:
            return 'decrescente'
        i += 1
    return 'nenhum'