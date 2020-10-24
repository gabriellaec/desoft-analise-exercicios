def classifica_lista(lista):
    n = len(lista)
    if n < 2:
        return 'nenhum'
    elif n >= 2:
        for i in range (0,n):
            if lista[i+1]>lista[i]:
            return 'crescente'
        for i in range (0,n):
            if lista[i+1]<lista[i]:
            return 'decrescente'
    else:
        return 'nenhum'