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
    lista = []
    numeros = list(range(0,1000000))
    while len(lista) == (n-1):
        if eh_primo(numeros[i]) == True:
            lista.append(numeros[i])
            i = i + 1
        else:
            i = i + 1
    return lista

        