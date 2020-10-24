def classifica_lista (lista):
    if len(lista) < 2:
        return 'nenhum'
    crescente = True
    decrescente = True
    i = 1
    while i < len(lista):
        if lista[i+1] > lista[i]:
            decrescente = False
        if lista[i+1] < lista[i]:
            crescente = False
        i = i + 1
    if decrescente == False:
        return 'crescente'
    elif crescente == False:
        return 'decrescente'
    elif decrescente == False and crescente == False:
        return 'nenhum'
    