def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    i = 0
    while i<len(lista): 
        if lista[i+1] > lista[i]:
            return 'crescente'
        elif lista[i+1] < lista[i]:
            return 'decrescente'
        else:
            return 'nenhum'
        