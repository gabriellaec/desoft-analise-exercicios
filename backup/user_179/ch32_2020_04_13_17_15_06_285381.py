def eh_primo (n):
    i = 3
    if n == 2:
        return True
    elif n == 0 or n == 1 or n%2 == 0:
        return False
    elif n < 0:
        return False
    else:
        while i < n:
            if n%i == 0:
                return False
            i = i + 2
        return True
    
def lista_primos (n):
    i = 0
    lista = range(0,n)
    while i < len(lista):
        if eh_primo(lista[i]) == True:
            i = i + 1
        else:
            lista.remove(lista[i])
            i = i + 1
    return lista