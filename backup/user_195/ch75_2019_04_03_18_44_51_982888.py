def verifica_primos(L):
    dici={}
    i=0
    while i<len(L):
        primo=True
        d=2
        if L[i]<2:
            primo=False
        elif L[i]==2:
            primo=True
        else:
            while d<L[i]:
                if L[i]%d==0:
                    primo=False
                d+=1
        L[i]=str(L[i])
        dici[L[i]]=primo
        i+=1
    return dici