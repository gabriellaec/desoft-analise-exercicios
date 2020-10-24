def verifica_primos(l):
    lf={}
    for v in l:
        for i in range(v-1):
            if v%i==0:
                lf[v]='nao é primo'
        lf[v]='primo'
    return lf
            
        