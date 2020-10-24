def classifica_lista(lista):
    i=0
    while i<len(lista):
        if lista[i-1]<lista[i]:
            i+=1
            return 'crescente'
        elif lista[i-1]>lista[i]:
            return 'decrescente'
        else:
            return 'nenhum'
    if len(lista)<2:
        return 'nenhum'