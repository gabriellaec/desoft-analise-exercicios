def verifica_progressao(l):
    c=1
    ca=1
    d=l[1]/l[0]
    e=l[1]-l[0]
    for i in range(2, len(l)):
        a=l[i-1]
        b=l[i]
        if a!=0:
            q=b/a
            r=b-a
            if q==d:
                c+=1
            if r==e:
                ca+=1
    if c==len(l) and ca==len(l):
        return 'AG'
    elif c==len(l):
        return 'PG'
    elif ca==len(l):
        return 'PA'
    else:
        return 'NA'
