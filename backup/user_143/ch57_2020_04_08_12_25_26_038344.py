def verifica_progressao(l):
    somaPA=(l[0]+l[len(l)-1])*(len(l))/2
    i=0
    soma=0
    q=l[i+1]/l[i]
    if q==1:
        somaPG==n*l[0]
    else:
        somaPG=l[0]*((q**len(l))-1)/(q-1)
    for p in l:
        soma+=p
    if soma==somaPA and soma==PG:
        return 'AG'
    elif soma==somaPG:
        return 'PG'
    elif soma==somaPA:
        return 'PA'
    else:
        return 'NA'
        
        