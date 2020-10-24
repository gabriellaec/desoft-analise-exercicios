def eh_primo (n):
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == -1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    else:
        i=3
        primu=True
        while i<n and primu:
            if n%2==0:
                primu = False
                return False
            elif n%i!=0:
                i=i+2
            elif n%i==0:
                primu = False
                return False
        if i>=n:
            return True
            
def verifica_primo(lista):
    checa_primo = {}
    for e in lista:
        booll = eh_primo(e)
        checa_primo[e] = booll
    return checa_primo
