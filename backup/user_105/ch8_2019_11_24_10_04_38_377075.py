def verifica_progressao(x):
    i = 0 
    while i <= len(x)-2: 
        if x[i]+x[i+2]==x[i+1]*2 and  x[i]*x[i+2]==x[i+1]**2:
            return 'AG'
        elif x[i]*x[i+2]==x[i+1]**2:
            return 'PG'
        elif x[i]+x[i+2]==x[i+1]*2:
            return 'PA'
        else:
            return 'NA'
        i+=1