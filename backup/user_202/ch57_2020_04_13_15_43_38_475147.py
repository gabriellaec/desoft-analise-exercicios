def verifica_progressao(x):
    if len(x) == 0:
        return 'NA'
    for n in range(len(x)-1):
        if (x[n+1] - x[n]) == (x[n-1]-x[n-2]) or x[n] == 0:
            return 'PA'
        elif (x[n+1] / x[n]) == (x[n-1] / x[n-2]):
            return 'PG'
        else:
            return 'NA'

    