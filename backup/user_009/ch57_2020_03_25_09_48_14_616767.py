def verifica_progressao(l):
    q = l[1]/l[0]
    n = len(l)
    v = 0
    if (l[0]+l[-1])*len(l)/2 == sum(l):
        v +=1
    if l[0]*((1-q**n)/(1-q))== sum(l):
        v+=2
    if v == 1:
        return 'PA'
    elif v ==2:
        return 'PG'
    elif v == 3:
        return 'GA'
    else:
        return 'NA'