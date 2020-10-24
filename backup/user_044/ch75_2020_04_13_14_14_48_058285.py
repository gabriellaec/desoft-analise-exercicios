def eh_primo(n):
    b=2
    z=True
    if n==2:
        return True
    elif n==0 or n==1:
        return False
    else:
        while b!=n and z:
            a=n%b
            b+=1
            if a==0:
                z=False
                return False
            elif b==n and a!=0:
                return True
            
def verifica_primos(lista):
    dn={}
    x=0
    for i in range(len(lista)):
        x=bool(eh_primo(lista[i]))
        dn[lista[i]]=x
    return dn