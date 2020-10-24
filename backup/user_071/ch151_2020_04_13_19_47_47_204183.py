def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    if len(lista)<2:
        return 'nenhum'
    for i in lista:
        if lista == sorted(lista):
            return 'crescente'
        if lista == sorted(lista, reverse = True):
            return 'decrescente'
        else:
            return 'nenhum'