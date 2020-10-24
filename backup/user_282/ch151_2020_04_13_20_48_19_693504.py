def classifica_lista(lista):
    count = 0
    for e in range(len(lista)):
        if lista[e] > count:
            count = lista[e]
            return 'crescente'
        elif lista[e] < count:
            count = lista[e]
            return 'decrescente'
        else:
            return 'nenhum'