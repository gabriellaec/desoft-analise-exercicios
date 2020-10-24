def eh_primo (x):
    if x==2:
        return True
    elif x==1 or x==0:
        return False
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n=n+2
        else: 
            return True
def verifica_primos(listanumint):
    dicionario=dict()
    i=0
    while i<len(listanumint):
        num = eh_primo(listanumint[i])
        if num==True:
            dicionario[listanumint[i]]=True
        else:
            dicionario[listanumint[i]]=False
    return dicionario
        