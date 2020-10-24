def classifica_lista(lista1):
    if len(lista1) < 2:
        return 'nenhum'
    
    n = lista1[1]-lista1[0]
    if n > 0:
        for i in range (len(lista1)-1):
            if lista1[i+1] - lista1[i] <= 0:
                return 'nenhum'
    if n < 0:
        for i in range (len(lista1)-1):
            if lista1[i+1] - lista1[i] >= 0:
                return 'nenhum'
    if n==0:
        return 'nenhum'
    elif n<0:
        return 'decrescente'
    elif n>0:
        return 'crescente'