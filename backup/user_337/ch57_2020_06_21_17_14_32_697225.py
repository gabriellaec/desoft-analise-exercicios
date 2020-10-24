def verifica_progressaao(lista):
    pa = []
    pg = []
    na = []
    for i in range(len(lista)-1):
        if lista[i+1]-lista[i] == lista[i+2] - lista[i+1]:
            pa.append(i)
        elif (lista[i+1])/(lista[i]) == (lista[i+2]) / (lista[i+1]):
            pg.append(i)
        else:
            na.append(i)
    if len(pa) == len(lista):
        return 'PA'
    elif len(pg) == len(lista):
        return 'PG'
    elif len(na) == len(lista):
        return 'NA'
    else:
        return 'AG'