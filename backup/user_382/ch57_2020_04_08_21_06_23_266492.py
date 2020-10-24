def verifica_progressao(lista):
    if lista == []:
        return 'NA'
    if len(lista) < 3:
        return 'NA'
    r = lista[1] - lista[0]
    q = lista[1]/lista[0]
    pa = True
    pg = True
    for i in range(len(l)-1):
        if r != l[i+1] - l[i]:
            pa = False
    
    for i in range(len(l)-1):
        if q != l[i+1]/l[i]:
            pg = False
    
    if pg == True and pa == True:
        return 'AG'
    if pg == True:
        return 'PG'
    if pa == True:
        return 'PA'
    else:
        return 'NA'
    