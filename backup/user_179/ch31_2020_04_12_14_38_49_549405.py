def eh_primo (numero):
    if numero%2 == 0 and numero != 2:
        return False
    else: 
        i = 3
        while i <= numero:
            if numero%i == 0:
                return False
            else:
                i = i + 2
        return True
        