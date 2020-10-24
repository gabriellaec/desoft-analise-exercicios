def verifica_progressao(x):
    c = True
    for i in x:
        if i == 0:
            c = False
            if x[2]-x[1] == x[1]-x[0]:
                return 'PA'
            else:
                return 'NA'
    if x[2]-x[1] == x[1]-x[0]:
        return 'PA'
    elif x[2]/x[1] == x[1]/x[0]:
        return 'PG'
    else:
        return 'NA'

    