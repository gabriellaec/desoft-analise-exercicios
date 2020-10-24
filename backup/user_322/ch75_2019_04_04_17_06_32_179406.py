def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 2 != 0:
        i = 3
        while i < n:
            if n % i != 0:
                i = i + 2
            else:
                return False
        return True
        
    return True

def verifica_primos(o): 
    dicionario = {}
    for i in o:
        if eh_primo(i) == True:
            dicionario[i] = True
        else:
            dicionario[i] = False
    return dicionario