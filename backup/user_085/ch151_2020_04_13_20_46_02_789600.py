def classifica_lista(list):
    n = 0
    for i in list:
        n += 1
        if list[n-1] < list[n]:
            return 'crescente'
        elif list[n-1] > list[n]:
            return 'decrescente'
        elif len(list)< 2:
            return 'nenhum'
        else:
            return 'nenhum'