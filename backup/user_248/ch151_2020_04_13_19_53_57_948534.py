def classifica_lista(lista):
    l=sorted(lista)
    if len(lista)<2:
        return 'nenhum'
    elif lista==l:
        return 'crescente'
    elif lista==seq.reverse(l):
        return 'decrescente'
    else:
        return 'nenhum'
    