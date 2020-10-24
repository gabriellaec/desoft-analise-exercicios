def eh_primo(num):
    if num!=0 and num!=1:
        if num%2==0:
            i=num-1
        else:
            i=num-2
        while i>1:
            if num%i!=0 and num%2!=0:
                i-=2
            else:
                return False
        return True
    else:
        return False
def lista_primos(n):
    lista=[]
    np=0
    while np<=n:
        if eh_primo(np)==True:
            lista.append(np)
        np+=1
    return lista