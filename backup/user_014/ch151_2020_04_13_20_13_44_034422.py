def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    elif len(lista) < 2:
        return 'nenhum'
    i = 0
    for i in range(lista):
        if lista[i] < lista[i+1]:
            return 'crescente'
        elif lista[i] > lista[i+1]:
            return 'decrescente'
        else:
            return 'nenhum'