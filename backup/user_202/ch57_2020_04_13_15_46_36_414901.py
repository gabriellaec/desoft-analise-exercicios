def verifica_progressao(x):
    a = True
    for i in x:
        if i == 0:
            c = False
    if len(x) == 0:
        return 'NA'
    for n in range(len(x)-1):
        if (x[n+1] - x[n]) == (x[n-1]-x[n-2]) and (x[n+1] / x[n]) == (x[n-1] / x[n-2]):
            return 'AG
        elif (x[n+1] - x[n]) == (x[n-1]-x[n-2]):
            return 'PA'
        elif (x[n+1] / x[n]) == (x[n-1] / x[n-2]):
            return 'PG'
        else:
            return 'NA'

    