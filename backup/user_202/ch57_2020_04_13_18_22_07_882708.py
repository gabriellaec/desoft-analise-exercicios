def verifica_progressao(lista):
    if len(lista) == 0:
        return 'NA'
    soma = lista[1]-lista[0]
    pa = True
    pg = True
    zero = False
    ret = 'NA'
    for i in lista:
        if i == 0:
            zero = True
    if zero == False:
        mult = lista[1]/lista[0]
        #PA PG AG ou NA
        for n in range(len(lista)-1):
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
        #PA ou NA
        for i in range(len(lista)-1):
            if lista[n+1]-lista[n] != soma:
                pa = False
        if pa == True:
            ret = 'PA'
        else:
            ret = 'NA'
    return ret