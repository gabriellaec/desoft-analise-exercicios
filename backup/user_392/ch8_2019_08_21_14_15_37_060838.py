def verifica_progressao(x):
    i=0
    PA = True
    PG = True
    while i<len(x)-2:
        if not 2*x[i+1] == x[i]+x[i+2]:
            PA = False
        if not x[i+1]**2 == x[i]+x[1+2]:
            PG = False
        i +=1
    if PG = True and PA = True:
        return 'AG'
    elif PG = True and PA = False:
        return 'PG'
    elif PG = False and PA = True:
        return 'PA'
    else:
        return 'NA'
        
        
        
        