def classifica_lista(lista):
    i=0
    if len(lista)<2:
        return 'nenhum'
    while i<len(lista):
        if lista[i+1]<lista[i]:
            i+=1
            return 'crescente'
        elif lista[i-1]>lista[i]:
            i+=1
            return 'decrescente'
        else:
            return 'nenhum'