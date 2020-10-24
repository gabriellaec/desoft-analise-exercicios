def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    elif len(lista) < 2:
        return 'nenhum'
    i = 0
    while i < len(lista):
        if lista[i] < lista[i+1]:
            return 'crescente'
        elif lista[i] > lista[i+1]:
            return 'decrescente'
        else:
            return 'nenhum'
        i += 1