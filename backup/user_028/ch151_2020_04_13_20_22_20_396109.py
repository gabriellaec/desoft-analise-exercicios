def classifica_lista(lista):
    i=0
    while i<len(lista):
        if lista[i]<lista[i+1]:
            i+=1
            return 'crescente'
        elif lista[i]>lista[i+1]:
            return 'decrescente'
        else:
            return 'nenhum'
    if len(lista)<2:
        return 'nenhum'