def classifica_lista(lista):
    if len(lista) <= 2:
        return ‘nenhum’
    
    if lista[0] < lista[1]:
        crescente = True
        for i in range(len(lista)):
            if i != 0:
                if lista[i] < lista[i-1]:
                    crescente = False
    
    elif lista[0] > lista[1]:
        decrescente = True
        for i in range(len(lista)):
            if i != 0:
                if lista[i] > lista[i-1]:
                    decrescente = False
    
    if crescente:
        return ‘crescente’
    
    if decrescente:
        return ‘decrescente’
    
    if not crescente and not decrescente:
        return ‘nenhum’