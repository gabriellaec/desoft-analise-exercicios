def classifica_lista(lista):
    if len(lista)< 2:
        return 'nenhum'
    i = 0
    while i < len(lista):
        if lista[i] > lista[i+1]:
            if lista[i]<lista[i+1]:
                return 'nenhum'
            return 'decrescente'
        if lista[i] < lista [i+1]:
            if lista[i]>lista[i+1]:
                return 'nenhum'
            return 'crescente'