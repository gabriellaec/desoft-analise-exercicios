def eh_primo(numero):
    if numero == 2:
        return True
    elif numero < 2:
        return False
    elif numero % 2 == 0:
        return False
    n = 3 
    while n< numero:
        if numero % n == 0:
            return False
        n+=2
    return True


def verifica_primos(lista):
    dicionario = {}
    for i in lista:
        if eh_primo(lista[i]) == True:
            dicionario[lista[i]] = True
        else:
            dicionario[lista[i]]= False
    return dicionario
    