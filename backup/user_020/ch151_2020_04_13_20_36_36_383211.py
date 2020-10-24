def classifica_lista(lista):
    i = 0
    n = 1
    if len(lista) < 2:
        return('nenhum')
    for i in range(len(lista)):
        if lista[i] < lista[n+1]:
            return('crescente')
        elif lista[i] > lista[n+1]:
            return('decrescente')
        elif lista == []:
            return('nenhum')
        else:
            return('nenhum')
        i += 1
        n += 1