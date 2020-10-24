def classifica_lista (lista):
    if len(lista)<2:
        return 'nenhum'
    crescente = True
    decrescente = True
    i = 0
    while i < len(lista)-2:
        if lista[i+1] > lista[i]:
            decrescente = False
        if lista[i+1] < lista[i]:
            crescente = False
        else:
            decrescente = False
            crescente = False
        i = i + 1
        if decrescente == False:
            return 'crescente'
        if crescente == False:
            return 'decrescente'
        if decrescente == False and crescente == False:
            return 'nenhum'
    