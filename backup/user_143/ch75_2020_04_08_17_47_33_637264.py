def eh_primo (perg):
    if perg==1 or perg==0:
        return False
    elif perg==2:
        return True
    elif perg>1:
        if perg%2==0:
            return False
        else:
            impar=3
            invalid=True
            while invalid:
                if impar<perg and perg%impar ==0:
                    return False
                elif impar==perg:
                    return True
                    invalid=False
                impar+=2
def verifica_primos(l):
    dici={}
    for i in l:
        x=eh_primo(i)
        if x==True:
            dici[i]=True
        else:
            dici[i]=False
    return dici
    