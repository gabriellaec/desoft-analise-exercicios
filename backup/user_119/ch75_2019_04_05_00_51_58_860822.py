def verifica_primos(p):
    dicio={}
    p[i]=int(p[i])
    while i<len(p):
        div=2
        primo=True
        if p[i]<2:
            dicio[p[i]]=False
        elif p[i]==2:
            dicio[p[i]]=True
        else:
            while div<p[i]:
                if p[i]%div==0:
                    primo=False
                div+=1
            dico[p[i]]=primo
        i+=1
    return dicio
        