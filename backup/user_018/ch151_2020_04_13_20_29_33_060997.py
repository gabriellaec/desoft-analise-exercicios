def classifica_lista(lista):
    lista_crescente = sorted(lista, key=int)
    lista_decrescente = sorted(lista, key = int, reverse = True)
    if len(lista) < 2:
        return 'nenhum'
    elif lista == lista_crescente:
        return 'crescente'
    elif lista == lista_decrescente:
        return 'decrescente'
    else:
        return 'nenhum'