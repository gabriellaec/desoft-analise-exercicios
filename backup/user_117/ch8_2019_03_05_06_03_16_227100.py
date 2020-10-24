def verifica_progresso(a,r,n):
    if a(n)==a(1)+(n-1)*r:
        return 'PA'
    elif a(n)==a(1)*r**(n-1):
        return 'PG'
    elif a(1)+(n-1)*r==a(1)*r**(n-1):
        return 'AG'
    else:
        return 'NA'
        