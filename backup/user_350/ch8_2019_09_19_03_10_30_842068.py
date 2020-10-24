def verifica_progressao(n):
    while i=True:
        if n[i]*2=n[i-1]+n[i+1]:
            return 'PA'
        if n[i]**2=n[i-1]*n[i+1]:
            return 'PG'
        else:
            return 'AG'