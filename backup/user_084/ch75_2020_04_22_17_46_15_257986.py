def verifica_primos(l):
    lf={}
    for v in l:
        for i in range(1,v):
            if v%i==0 or v==1 or v==0 or v<0:
                lf[v]='nao é primo'
        lf[v]='primo'
    return lf
            
        