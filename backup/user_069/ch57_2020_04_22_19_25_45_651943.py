def classifica_progressao (lista):

    if len(lista) < 2:
        return 'NA'

    elif len(lista) == 2:
        return 'AG'
    
    razao_pa = lista[1] - lista[0] 
    razao_pg = lista[1]/lista[0]

    pa = False
    pg = False 

    for i in range(len(lista)-1):
        if lista[i+1] - lista[i] == razao_pa:
            pa = True
        elif lista[i+1]/lista[i] == razao_pg:
            pg = True
    
    if pa == True:
        return 'PA'

    elif pg == True:
        return 'PG'

    elif pa == True and pg == True:
        return 'AG'

    else: 
        return 'NA'