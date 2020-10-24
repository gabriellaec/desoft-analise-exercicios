def classifica_lista (lista):
    i=1
    while i<len(lista):
        if lista[i-1]<lista[i]:
            i+=1
            return 'decrescente'
        elif lista [i-1]>lista[1]:
            i+=1
            return 'crescente'
        else:
            return 'nenhum'
        