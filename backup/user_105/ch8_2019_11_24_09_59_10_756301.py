def verifica_progressao(x):
    
    if x[0]+x[2]==x[1]*2 and  x[0]*x[2]==x[1]**2:
        return 'AG'
    elif x[0]*x[2]==x[1]**2:
        return 'PG'
    elif x[0]+x[2]==x[1]*2 :
        return 'PA'
    else:
        return 'NA'