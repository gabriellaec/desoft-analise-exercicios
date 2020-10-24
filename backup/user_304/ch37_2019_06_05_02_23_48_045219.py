def eh_primo (numero):
    if numero<=1:
        return False
    if numero%2==0 and numero!=2:
        return False
    eh_primo = True
    i=2
    while i<numero:
        if numero%i==0:
            eh_primo = False
        i=i+1
    return eh_primo

def lista_primos(n):
    nprimos=[]
    i=0
    while len(nprimos)<n:
        if eh_primo(i)==True:
            nprimos.append(i)
        i+=1
    return nprimos