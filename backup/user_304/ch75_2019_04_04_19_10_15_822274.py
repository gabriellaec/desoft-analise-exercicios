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

def verifica_primos(numeros):
    primos={}
    for e in numeros:
        if eh_primo(e)==True:
            primos[e]=True
        else:
            primos[e]=False
    return primos