def verifica_progressao(l):
    s=0
    k=l[1]
    t=l[0]
    p=k/t
    w=k-t
    r=0
    q=0
    for i in range(1, len(l)):
        s=l[i-1]
        r=l[i]-s
        q=(l[i]/s)
        if r==w:
            return 'PA'
        elif q==p:
            return 'PG'
        elif r==w and q==p:
            return 'AG'
        else:
            return 'NA'