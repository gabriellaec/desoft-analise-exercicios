def verifica_primos(l):
    DICI={}
    primo=False
    for i in range(len(l)):
        I=l(i)
        for j in range(I):
            if I%j!=0:
                primo=True
            else:
                pass
        DICI[l(i)]=primo
    return DICI
        
