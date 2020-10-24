def verifica_progressao(l):
    for i in range(2, len(l)):
        if (l[i] - l[i-1]) == (l[i-1] - l[i-2]) and (l[i]/l[i-1]) == (l[i-1]/l[i-2]):
            return 'AG'
        elif (l[i] - l[i-1]) == (l[i-1] - l[i-2]):
            return 'PA'
        elif (l[i]/l[i-1]) == (l[i-1]/l[i-2]):
            return 'PG'
        else:
            return 'NA'