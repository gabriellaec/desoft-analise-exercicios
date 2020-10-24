def classifica_lista(lista):
    i = 0
    for i in range(lista):
        if lista[i+1] > lista[i]:
            return 'crescente'
        elif lista[i+1] < lista[i]:
            return 'decrescente'
        elif len(lista) < 2:
            return 'nenhum'
        else:
            return 'nenhum'