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
                
def primos_entre (a,b):
    primoab=[]
    i=0
    while a+i==eh_primo and a+i<=b
        primoab.append (a)
        i=i+1
    return primoab
        