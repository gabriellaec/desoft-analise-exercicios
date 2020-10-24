def classifica_lista(lista):
    i=0
    if len(lista)<2 or lista[i+2]<=lista[i+1]>=lista[i] :
        return 'nenhum'
    elif lista[i+1] <= lista[i]:
        return 'decrescente'
    else:
        return 'crescente'
    