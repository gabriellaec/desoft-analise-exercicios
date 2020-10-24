def classifica_lista(lista):

    if len(lista) < 2:
        return 'nenhum'
    
    dif = lista[1] - lista[0]
    for e in range(len(lista) - 1):
        teste = lista[e + 1] - lista[e]
        if teste != dif:
            return 'nenhum'
    if dif > 0:
        return 'crescente'
    elif dif < 0:
        return 'decrescente'