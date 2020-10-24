def verifica_progressao(l):
    somaPA=(l[0]+l[len(l)-1])*(len(l))/2
    r=l[1]-l[0]
    soma=0
    q=l[1]/l[0]
    if q==1:
        somaPG==len(l)*l[0]
    else:
        somaPG=l[0]*((q**len(l))-1)/(q-1)
    w=1
    x=1
    for p in l:
        soma+=p
        r1=p-w
        if w!=0:
            q1=p/w
        w=p
    if soma==somaPA and soma==PG and r==r1 and q==q1:
        return 'AG'
    elif soma==somaPG and q=q1:
        return 'PG'
    elif soma==somaPA and r==r1:
        return 'PA'
    else:
        return 'NA'
        
        