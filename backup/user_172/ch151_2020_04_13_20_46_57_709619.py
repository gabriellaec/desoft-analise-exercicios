def classifica_lista(lista):
    n = len(lista)
    if n < 2:
        return 'nenhum'
    elif n >= 2:
        for i in range (1,n):
            if lista[i]>lista[i-1]:
                c = lista
                #return 'crescente'
        for i in range (1,n):
            if lista[i]<lista[i-1]:
                d = lista
                #return 'decrescente'
        if lista == c:
            return 'crescente'
        elif lista == d:
            return 'decrescente'
    else:
        return 'nenhum'