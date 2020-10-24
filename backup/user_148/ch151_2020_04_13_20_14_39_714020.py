def classifica_lista(lista):
    lista = []

    if len(lista)>2:
        if lista == lista.sort():
            lista.sort()
            return 'crescente'
        elif lista == lista.sort(reverse=True):
            lista.sort(reverse=True)
            return 'decrescente'
        else:
            return 'nenhum'
    else:
        return 'nenhum'
