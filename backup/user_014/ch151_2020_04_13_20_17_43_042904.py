def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    elif len(lista) < 2:
        return 'nenhum'
    i = 0
    n = 1
    for i,n in range(len(lista)):
        if lista[i] < lista[i+1]:
            return 'crescente'
        elif lista[i] > lista[i+1]:
            return 'decrescente'
        elif lista[i+1] > lista[i+n] or lista[i+1] < lista[i+n]:
            return 'nenhum'
        else:
            return 'nenhum'