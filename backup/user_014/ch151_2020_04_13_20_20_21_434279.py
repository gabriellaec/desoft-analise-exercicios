def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    elif len(lista) < 2:
        return 'nenhum'
    i = 0
    n = 1
    for i in range(len(lista)):
        if lista[i] < lista[i+1]:
            return 'crescente'
        elif lista[i] > lista[i+1]:
            return 'decrescente'
        else:
            return 'nenhum'
    for n in range(len(lista):
        if lista[n] > lista[n+1] or lista[n] < lista[n+1]:
           return 'nenhum'