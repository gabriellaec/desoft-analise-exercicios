def classifica_lista(l):
    if len(l) < 2:
        return 'nenhum'
    crescente = 1
    decrescente = 1
    for i in (len(l)-1):
        if l[i+1] > l[i]:
            decrescente = 0
        if l[i+1] < l[i]:
            crescente = 0
    if crescente = 1:
        return 'crescente'
    elif decrescente = 1:
        return 'decrescente'
    else:
        return 'nenhum'
            
        