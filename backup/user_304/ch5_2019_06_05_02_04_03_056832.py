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

def maior_primo_menor_que(n):
    if n<=1:
        return -1
    else:
        i=n
        while eh_primo (i)!= True:
            i-=1
        return i
    