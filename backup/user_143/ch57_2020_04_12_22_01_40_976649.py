def verifica_progressao(l):
    a=l[0]
    c=1
    ca=1
    d=0
    e=0
    for i in range(1, len(l)):
        b=l[i]
        if a!=0:
            q=b/a
            r=b-a
            if q==d:
                c+=1
            if r==e:
                ca+=1
        d=q
        e=r
        a=b
    if c==len(l) and ca==len(l):
        return 'AG'
    elif c==len(l):
        return 'PG'
    elif ca==len(l):
        return 'PA'
    else:
        return 'NA'
