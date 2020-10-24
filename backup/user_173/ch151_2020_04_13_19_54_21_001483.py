def classifica_lista (lista):
    lista =[]
    for i in lista:
        if len(lista) < 2  lista != sorted(lista) and lista != sorted(lista,reverse = True):
            return 'nenhum'
        elif lista != sorted(lista) and lista != sorted(lista,reverse = True):
            return 'nenhum'
        elif lista == sorted(lista):
            return 'crescente'
        elif lista == sorted(lista,reverse = True):
            return 'decrescente'
    