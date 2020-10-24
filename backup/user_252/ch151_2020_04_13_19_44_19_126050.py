def classifica_lista(lista):
    i=1
    n=len(lista)
    while n<2:
        return 'nenhum'
    while i<n:
        if lista[i-1]<lista[i]:
            i+=1
            return 'crescente'
        elif lista[i-1]>lista[i]:
            i+=1
            return 'decrescente'
        else:
            return 'nenhum'