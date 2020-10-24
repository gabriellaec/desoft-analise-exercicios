def verifica_progressao(l):
    n=len(l)
    c=len(l)-1
    if (l[n]-l[0])==l[c]-l[1]:
        return 'PA'
    if l[n]/l[0]==l[c]/l[1]:
        return 'PG'
    if (l[n]-l[0])==l[c]-l[1] and l[n]/l[0]==l[c]/l[1]:
        return 'AG'
    else:
        return 'NA'
    
    