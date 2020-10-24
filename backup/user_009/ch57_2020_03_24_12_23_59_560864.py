def verifica_progressao(l):
    if l[2] - l[1]  == l[1] - l[0] and l[2]/l[1]  == l[1]/l[0]:
        return 'GA'
    elif l[2]/l[1]  == l[1]/l[0]:
        return 'PG'
    elif l[2] - l[1]  == l[1] - l[0]:
        return 'PA'
    else:
        return 'NA'
