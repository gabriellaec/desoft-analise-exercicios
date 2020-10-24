def verifica_progressao(lista):
    if len(lista) == 0:
        return 'NA'
    pa = True
    pg = True
    zero = False
    ret = 'NA'
    for i in lista:
        if i == 0:
            zero = True
    if zero == False:
        soma = lista[1]-lista[0]
        mult = lista[1]/lista[0]
        for n in len(lista)-1:
            if lista[n+1]-lista[n] != soma:
                pa = False
            if lista[n+1]/lista[n] != mult:
                pg = False
        if pg == True and pa == True:
            ret = 'AG'
        elif pg == True:
            ret = 'PG'
        elif pa == True:
            ret = 'PA'
        else:
            ret = 'NA'
    else:
        soma = lista[1]-lista[0]
        for i in len(lista)-1:
            if lista[n+1]-lista[n] != soma:
                pa = False
        if pa == True:
            ret = 'PA'
        else:
            ret = 'NA'
    return ret
        
        
    

    