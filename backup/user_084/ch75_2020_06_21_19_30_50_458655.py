def verifica_primos(l):
    DICI={}
    primo=False
    for i in range(len(l)):
        I=l(i)
        j=2
        while j>l(i):
            if I%j!=0:
                primo=True
                j+=1
            else:
                pass
                j+=1
        DICI[l(i)]=primo
    return DICI
        
