def classifica_lista(lista):
    lista = []
    x = lista.sort()
    y = lista.sort(reverse=True)

    if len(lista)>1:
        if lista == x:
            return 'crescente'
        elif lista == y:
            return 'decrescente'
        else:
            return 'nenhum'
    else:
        return 'nenhum'
