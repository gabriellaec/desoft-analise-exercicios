def verifica_progressao(l):
    somaPA=(l[0]+l[len(l)-1])*(len(l))/2
    i=0
    soma=0
    if (l[i+1]/l[i])==(l[len(l)-1]/l[len(l)-2]):
        q=l[i+1]/l[i]
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
        
        