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
def lista_primos(n):
    lista=[]
    i=0
    a=0
    while i<=n:
        if eh_primo(a):
            lista.append(a)
            i+=1
            a+=1
            lista.sort()
        else:
            a+=1
    return lista
        
