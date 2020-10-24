def classifica_lista (lista_numeros):
    if len(lista_numeros) < 2:
        return 'nenhum'
    for x in lista_numeros:
        if lista_numeros == sorted(lista_numeros,reverse = True):
            return 'decrescente'
        elif lista_numeros == sorted(lista_numeros):
            return 'crescente'
        else:
            return 'nenhum'
    