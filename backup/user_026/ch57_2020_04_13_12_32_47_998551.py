def verifica_progressao(lista):
    if lista == [] :
        return 'NA'
    if len(lista) < 3:
        return 'NA'
    for i in lista:
        if i == 0:
            return 'NA'
        
    r = lista[1] - lista[0]
    q = lista[1]/lista[0]
    pa = True
    pg = True
    
    for i in range(len(lista)-1):
        if r != lista[i+1] - lista[i]:
            pa = False
            
    for i in range(len(lista)-1):
        if q != lista[i+1]/lista[i]:
            pg = False
            
    if pg == True and pa == True:
        return 'AG'
    if pg == True:
        return 'PG'
    if pa == True:
        return 'PG'
    else:
        return 'AG'