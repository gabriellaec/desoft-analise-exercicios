def verifica_progressao(a,b,c):
    if (a+c)/2==b:
        return'PA'
    elif b/a==c/b:
        return'PG'
    elif (a+c)/2==b and b/a==c/b:
        return'AG'
    else:
        return'NA'
        