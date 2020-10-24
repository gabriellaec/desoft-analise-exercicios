def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    for i in lista:
        if lista == sorted(lista):
            return 'crescente'
        if lista == sorted(lista, reverse = True):
            return 'decrescente'
        else:
            return 'nenhum'