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
    
def primos_entre (a,b):
    entre = list(range(a,b))
    i = 0
    while a < b:
        if eh_primo(entre[i]) == True:
            a = a + 1
            i = i + 1
        else:
            lista.remove(a)
            a = a + 1
            i = i + 1
    return lista
        