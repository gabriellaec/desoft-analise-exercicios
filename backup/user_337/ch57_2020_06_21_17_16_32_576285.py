def verifica_progressao(lista):
    pa = []
    pg = []
    na = []
    for i in range(len(lista)-3):
        if lista[i+1]-lista[i] == lista[i+2] - lista[i+1]:
            pa.append(i)
        elif (lista[i+1])/(lista[i]) == (lista[i+2]) / (lista[i+1]):
            pg.append(i)
        else:
            na.append(i)
    if len(pa) == len(lista)-3:
        return 'PA'
    elif len(pg) == len(lista)-3:
        return 'PG'
    elif len(na) == len(lista)-3:
        return 'NA'
    else:
        return 'AG'