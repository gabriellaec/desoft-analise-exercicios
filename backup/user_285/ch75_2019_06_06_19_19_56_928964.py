def eh_primo(n):
    primo=True
    if n<=1:
        primo=False
    for e in range(2,n):
        if n%e==0 and e!=n:
        	primo=False
    return primo

def verifica_primos(lista):
    dic={}
    for i in lista:
        if eh_primo(i):
            dic[i]=True
        else:
            dic[i]=False
    return dic
            