def classifica_lista(lista):
    i = 0
    while i < len(lista):
        if lista[i+1] > lista[i]:
            return 'crescente'
            i += 1
        elif lista[i+1] < lista[i]:
            return 'decrescente'
            i += 1
        elif len(lista) < 2:
            return 'nenhum'
            i += 1
        else:
            return 'nenhum'
            i += 1
