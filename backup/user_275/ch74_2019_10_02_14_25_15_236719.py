def cria_bigramas(T):
    bigramas=[]
    i=0
    n=len(T)-1
    while i<n:
        B=T[i]+T[i+1]
        bigramas.append(B)
        i+=1
    return bigramas
ex="banana nanica"
print(cria_bigramas(ex))
def conta_bigramas(T):
    bigramas={}
    L=cria_bigramas(T)
    n = len(L)
    for i in range(n):
        bigramas[L[i]]=0
    for i in range(n):
        if L[i] in bigramas.keys():
            bigramas[L[i]]+=1
    return bigramas