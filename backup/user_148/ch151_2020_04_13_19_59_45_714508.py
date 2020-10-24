def classifica_lista(lista):
    
    if len(lista)>2:
        if lista.sort() is True:
            return 'crescente'
        elif lista.sort(reverse=True) is True:
            return 'decrescente'
        else:
            return 'nenhum'
    else:
        return 'nenhum'