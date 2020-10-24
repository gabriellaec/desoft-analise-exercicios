def verifica_progresso(x,r):
    x = []
    i = 0
    while i < len(x):
        if x[i+1] = x[i] + r:
            return 'PA'
        elif x[i+1] = x[i] * r:
            return 'PG'
        elif x[i+1] = x[i]*r or x[i+1] = x[i] + r:
            return  'AG'
        else:
            return 'NA'