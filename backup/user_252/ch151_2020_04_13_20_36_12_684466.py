def classifica_lista(lista):
    i=1
    n=len(lista)
    while lista<2:
        return 'nenhum'
    while i<len(lista):
        if lista[i-1]<lista[i]:
            i+=1
        else:
            return 'nenhum'
    return 'crescente'
    while i<len(lista):
        if lista[i-1]>lista[i]:
            i+=1
        else:
            return 'nenhum'
    return 'decrescente'