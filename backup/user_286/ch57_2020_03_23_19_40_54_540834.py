def verifica_progressao (lista):

    pa = True
    pg = True

    razao_pa = lista[1] - lista[0]
    for numero in lista:
        if numero != lista[0]:
            divisao_teste = lista[lista.index(numero)] - lista[lista.index(numero) - 1]
            if razao_pa != divisao_teste:
                pa = False
    
    razao_pg = lista[1] / lista[0]
    for numero in lista:
        if numero == 0:
            pg = False
            break
        if numero != lista [0]:
            divisao_teste = lista[lista.index(numero)] / lista[lista.index(numero) - 1]
            if razao_pg != divisao_teste:
                pg = False
    
    if pa and pg:
        return 'AG'

    elif pa:
        return 'PA'

    elif pg:
        return 'PG'

    else:
        return 'NA'
