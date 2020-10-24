def eh_primo (n):
    i = 3
    if n == 2:
        return True
    elif n == 0 or n == 1 or n%2 == 0:
        return False
    else:
        while i < n:
            if n%i == 0:
                return False
            i = i + 2
        return True
    
def verifica_primos (lista):
    i = 0
    dicionario = {}
    while i < len(lista):
        if eh_primo(lista[i]) == True:
            dicionario[lista[i]] == True
            i = i + 1
        else:
            dicionario[lista[i]] == False
            i = i + 1