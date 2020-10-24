def eh_primo (n):
    if n<2:
        return False
    if n==2:
        return True
    if n==3:
        return True
    if n==5:
        return True
    else:
        if n%2==0:
            return False
        else:
            i = 3
            while i<n:
                if n%i ==0:
                    return False
                else:
                    i+=2
            return True 

def verifica_primos (lista):
    dicionario = {}
    for i in lista:
        dicionario[i] = eh_primo(i)
    return dicionario
        