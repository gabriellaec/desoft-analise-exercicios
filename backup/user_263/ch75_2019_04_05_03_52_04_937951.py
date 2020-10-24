def eh_primo(n):
    if n==0 or n==1 or n==-1:
        return False
    elif n%2==0 and n!=2:
        return False
    else:
        i=3
        primo=True
        while i<n:
            if n%i==0:
                primo=False
            i+=2
        if primo==True:
            return True
        else:
            return False
        
def verifica_primos(numeros):
    dic={}
    for e in numeros:
        if e not in dic:
            dic[e]=eh_primo(e)
    return dic