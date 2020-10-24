def classifica_lista (lista):
    if len(lista)<2:
        return 'nenhum'
    i = len(lista) - 1
    while i > 0:
        if lista[i] > lista[i - 1]:
            return 'crescente'
        if lista[i] < lista[i-1]:
            return 'decrescente'
        else:
            return 'nenhum'
        i = i - 1
        
    