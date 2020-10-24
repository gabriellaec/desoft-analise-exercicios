def eh_primo (numero):
    if numero<=1:
        return 'não é primo'
    if numero%2==0 and numero!=2:
        return 'não é primo'
    eh_primo = True
    i=1
    while i<numero:
        if numero%i==0:
            eh_primo = False
        i=i+2
    if eh_primo:
        return 'é primo'
    else:
        return 'não é primo'
                