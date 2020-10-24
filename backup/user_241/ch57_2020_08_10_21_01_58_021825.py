def verifica_progressao(lista):
    if lista == [] or len(lista) < 3:
        return 'NA'
    for i in lista:
        if i == 0:
            return 'NA'
    x = lista[1] - lista[0]
    y = lista[1]/lista[0]
    pa = True
    pg = True
    for i in range(len(lista)-1):
        if x != lista[i+1] - lista[i]:
            pa = False 
        if y != lista[i+1]/lista[i]:
            pg = False
    if pg == True:
        return 'PG'
    if pa == True:
        return 'PA'
    if pa == True and pg == True:
        return 'AG'
    else:
        'NA'
    
    