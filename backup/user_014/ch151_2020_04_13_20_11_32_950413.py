def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    elif len(lista) < 2:
        return 'nenhum'
    i = 0
    while i < (len(lista)-1):
        if lista[i+1] > lista[i]:
            return 'crescente'
        elif lista[i+1] < lista[i]:
            return 'decrescente'
        else:
            return 'nenhum'
        i += 1