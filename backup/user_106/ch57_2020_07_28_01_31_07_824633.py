def verifica_progressao(lista):    
    if len(lista) == 1 or lista == []:
        return 'NA'
    elif len(lista) == 2:
        return 'AG'
    else:
        i = 0
        pg = True
        pa = True
        while i+2 < len(lista):
            if not lista[i+2] * lista[i] == lista[i+1] ** 2:
                pg = False
            if not lista[i+2] - lista[i+1] == lista[i+1] - lista[i]:
                pa = False
            i += 1
        if pg == False and pa == False:
            return 'NA'
        elif pg == True and pa == True:
            return 'AG'
        elif pg == True and pa == False:
            return 'PG'
        else:
            return 'PA'