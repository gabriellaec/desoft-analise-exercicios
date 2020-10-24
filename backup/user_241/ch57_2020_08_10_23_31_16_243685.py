def verifica_progressao(lista):
    if lista == [] and len(lista) < 3:
        return 'NA'
    pa = True
    pg = True
    if 0 in lista:
        y = 0
        pg = False
    else:
        y = lista[1]/lista[0]
    x = lista[1] - lista[0]
    for i in range(len(lista)-1):
        if x != lista[i+1] - lista[i]:
            pa = False 
        if lista[i+1] !=  y * lista[i]:
            pg = False  
    if pa == True and pg == True:
        return 'AG'    
    if pg == True:
        return 'PG'
    if pa == True:
        return 'PA'
    if pa == False and pg == False:
        return 'NA'
    
    