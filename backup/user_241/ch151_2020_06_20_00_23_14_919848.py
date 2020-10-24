def classifica_lista(lista):
    i = 1 
    decrescente = True
    crescente = True
    x = len(lista)
    if x < 2:
        return 'nenhum' 
    while i < x:
        if lista[i] < lista[i-1]:
            crescente = False
        if lista[i] > lista[i-1]:
            decrescente = False
        i = i + 1
    if crescente:
        return 'crescente' 
    elif decrescente:
        return 'decrescente'
    else:
        return 'nenhum'