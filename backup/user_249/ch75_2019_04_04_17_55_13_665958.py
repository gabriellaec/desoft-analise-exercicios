def verifica_primos(L):
    dicionario={}
    i=0
    divisor=2
    primo=True
    while i<len(L):
        if L[i]<2:
            dicionario[l[i]]=false
        elif L[i]==2:
            dicionario[L[i]]=True
        else:
            while divisor<l[i]:
                if L[i] % divisor==0:
                    primo=False
                divisor+=1
            dicionario[L[i]]=primo
return dicionario