def classifica_lista (lista):
    lista =[]
    for i in lista:
        if len(lista) < 2 or lista != sorted(lista) and lista != sorted(lista,reverse = True):
            return 'nenhum'
    elif lista == sorted(lista):
            return 'crescente'
    else:
        return 'decrescente'
    