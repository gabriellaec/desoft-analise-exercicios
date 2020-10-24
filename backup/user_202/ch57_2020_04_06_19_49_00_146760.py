def verifica_progressao(x):
    if x[2]-x[1] == x[1]-x[0]:
        r = 'PA'
    elif x[2]/x[1] == x[1]/x[0]:
        r = 'PG'
    else:
        r = 'NA'
    
    