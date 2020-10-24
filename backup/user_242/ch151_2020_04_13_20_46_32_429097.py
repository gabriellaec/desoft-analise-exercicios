def classifica_lista(lista):
    i=0
    if len(lista)<2 or lista[i]<=lista[i+1]>=lista[i+2]:
        return 'nenhum'
    elif lista[i+1] <= lista[i]:
        return 'decrescente'
    else:
        return 'crescente'
    