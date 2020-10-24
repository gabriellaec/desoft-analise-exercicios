def eh_primo(x):
    while x > 0:
        if x == 2:
            return True
        elif x == 0 or x == 1:
            return False
        elif x%2 == 0:
            return False
        else:
            i = 3
            while i < x:
                if x%i == 0:
                    return False
                i = i+2
            return True
    return False
def verifica_primos(lista):
    i = 0
    dicionario = {}
    while i < len(lista):
        if eh_primo(lista[i]):
            dicionario[lista[i]] = True
        else:
            dicionario[lista[i]] = False
        i +=1
    
    return dicionario