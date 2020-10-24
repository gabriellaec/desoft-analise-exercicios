def verifica_progressao (lista):

    if len(lista) < 2:
        return 'NA'

    elif len(lista) == 2:
        return 'AG'
    
    razao_pa = lista[1] - lista[0] 
    razao_pg = lista[1]/lista[0]

    pa = True
    pg = True

    while pa:
        for i in range(len(lista)-1):
            if lista[i+1] - lista[i] != razao_pa:
                pa = False
                break
        break

    while pg:
        for i in range(len(lista)-1):   
            if lista[i+1]/lista[i] != razao_pg:
                pg = False
                break
        break

    if pa == True and pg == True:
        return 'AG'

    elif pg == True:
        return 'PG'

    elif pa == True:
        return 'PG'

    else: 
        return 'NA'