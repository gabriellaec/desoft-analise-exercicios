def classifica_lista(lista):
    i=0
    if len(lista)<2:
        return 'nenhum'
    elif lista[i+1] <= lista[i]:
            return 'decrescente'
    else:
        return 'crescente'
    