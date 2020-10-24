def eh_primo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        if n%2 == 0:
            return False
        else:
            impar = 3
            while impar < n:
                if n%impar == 0:
                    return False
                impar = impar + 2
            return True

def verifica_primos(lista):
    dic = {}
    i = 0
    while i < len(lista):
        a = lista[i]
        booleano = eh_primo(a)
        dicionario [a] = booleano
        i += 1
    return dicionario