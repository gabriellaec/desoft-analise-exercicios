def classifica_lista(lista):
    i=1
    n=len(lista)
    while i<n:
        if n<2:
            return 'nenhum'
        if lista[i-1]<lista[i]:
            i+=1
            return 'crescente'
        elif lista[i-1]>lista[i]:
            return 'decrescente'
        else:
            return 'nenhum'
           