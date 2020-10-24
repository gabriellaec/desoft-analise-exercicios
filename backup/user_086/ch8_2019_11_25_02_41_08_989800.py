def verifica_progressao(lista):
    n=len(lista)
    soma = 0
    t=0
    for i in range(n):
        soma += lista[t]
        t+=1
        
    if soma==n*(lista[0]+lista[n])/2:
        PA = True
    if soma==lista[0]*((lista[1]/lista[0])**n-1)/(lista[1]/lista[0]):
        PG = True
        
    if PA and PG:
        return 'AG'
    if PA:
	    return 'PA'
    if PG:
        return 'PG'
    if not PA and not PG:
	    return 'NA'