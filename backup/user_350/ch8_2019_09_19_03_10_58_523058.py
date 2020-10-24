def verifica_progressao(n):
    i = True
    while i:
        if n[i]*2=n[i-1]+n[i+1]:
            return 'PA'
        if n[i]**2=n[i-1]*n[i+1]:
            return 'PG'
        else:
            return 'AG'