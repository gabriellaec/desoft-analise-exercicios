def eh_primo (numero):
    if numero<=1:
        return False
    if numero%2==0 and numero!=2:
        return False
    eh_primo = True
    i=1
    while i<numero:
        if numero%i==0:
            eh_primo = False
        i=i+2
    return eh_primo
                