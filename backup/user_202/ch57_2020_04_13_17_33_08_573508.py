def verifica_progressao(x):
    zero = False
    ret = 'NA'
    var = False
    if len(x) == 0:
        return 'NA'
    for i in x:
        if i == 0:
            zero = True
    for n in range(len(x)-1):
        if x[n+1]-x[n] == 0:
            ret = 'AG'
        else:
            var = True
    if vav == True:
        for n in range(len(x)-1):
        elif (x[n+1] - x[n]) == (x[n-1]-x[n-2]):
            ret = 'PA'
        elif (x[n+1] / x[n]) == (x[n-1] / x[n-2]):
            ret = 'PG'
        else:
            ret = 'NA'
    return ret
    
    

    