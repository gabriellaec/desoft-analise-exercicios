def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    c = True 
    d = False
    i = 1
    while i < len(lista):
        if lista[i-1] >= lista[i]:
            c = False
        if lista[i-1] <= lista[i]:
            d = False
        
        i += 1
    if c:
        return 'crescente'
    elif d:
        return 'decrescente'
        
 