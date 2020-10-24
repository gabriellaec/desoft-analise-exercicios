def verifica_progressao(lista):
    print(lista)
    if lista == []:
        return 'NA'
    if len(lista) < 3:
        return 'NA'
    for i in lista:
        if i == 0:
            return 'NA'
    indice_pa = lista[1] - lista[0]
    indice_pg = lista[1] / lista[0]
    pa = True
    pg = True
    for i in range(len(lista)-1):
        if lista[i+1] - lista[i] != indice_pa:
            pa = False
    for i in range(len(lista)-1):
        if lista[i+1] / lista[i] != indice_pg:
            pg = False
    if pa and pg:
        return 'AG'
    if pg:
        return 'PG'
    if pa:
        return 'PA'
    else:
        return 'NA'