def classifica_lista(lista):
    count = lista[0]
    for e in range(1, len(lista)):
        if lista[e] > count:
            count = lista[e]
            return 'crescente'
        elif lista[e] < count:
            count = lista[e]
            return 'decrescente'
        else:
            return 'nenhum'