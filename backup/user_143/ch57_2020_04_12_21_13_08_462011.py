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
    z=1
    for p in l:
        soma+=p
        if w!=0:
            if q1==x or z==r1: 
                q1=p/w
                r1=p-w
        w=p
        x=q1
        z=r1
    if soma==somaPA and soma==PG and r==r1 and q==q1:
        return 'AG'
    elif soma==somaPG and q=q1:
        return 'PG'
    elif soma==somaPA and r==r1:
        return 'PA'
    else:
        return 'NA'
        
        