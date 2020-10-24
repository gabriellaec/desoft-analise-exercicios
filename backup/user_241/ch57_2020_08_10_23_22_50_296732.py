def verifica_progressao(lista):
    if lista == []:
        return 'NA'
    elif len(lista) < 3:
        return 'AG'
    pa = True
    pg = True
    x = lista[1] - lista[0]
    y = lista[1]/lista[0]
    for i in lista:
        if i == 0:
            return 'NA'
    for i in range(len(lista)-1):
        if x != lista[i+1] - lista[i]:
            pa = False 
        if y != lista[i+1]/lista[i]:
            pg = False
          
    if pa == True and pg == True:
        return 'AG'    
    if pg == True:
        return 'PG'
    if pa == True:
        return 'PA'
    if pa == False and pg == False:
        'NA'
    
    