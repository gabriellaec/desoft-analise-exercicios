def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    
    crescente = True
    decrescente = True
    
    i = 0
    while i<len(lista):
        if lista[i+1] < lista[i]:
            crescente = False
        if lista[i+1] > lista[i]:
            decrescente = False
        i += 1
        
    if crescente:
        return 'crescente'
    elif decrescente:
        return 'decrescente'
    else:
        return 'nenhum'
