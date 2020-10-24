def verifica_progressao(l):
    n=len(l)
    if (l[n]-l[0])==l[n-1]-l[1]:
        return 'PA'
    if l[n]/l[0]==l[n-1]/l[1]:
        return 'PG'
    if (l[n]-l[0])==l[n-1]-l[1] and l[n]/l[0]==l[n-1]/l[1]:
        return 'AG'
    else:
        return 'NA'
    
    