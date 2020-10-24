classifica_lista (lista):
    lista =[]
    if len(lista) < 2:
        return 'nenhum'
    for i in lista:
        if lista == sorted(lista,reverse = True):
            return 'decrescente'
        elif lista == sorted(lista):
            return 'crescente'
        else:
            return 'nenhum'
    