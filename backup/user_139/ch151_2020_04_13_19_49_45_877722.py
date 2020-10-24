def classifica_lista (lista):
    if len(lista) < 2:
        return 'nenhum'
    i = 1
    while i < len(lista):
        if lista[i - 1] < lista[i]:
            return 'crescente'
            i += 1
        elif lista [i] < lista [i - 1]:
            return 'decrescente'
        else:
            return 'nenhum'
