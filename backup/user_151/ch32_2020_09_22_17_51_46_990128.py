def eh_primo(x):
    if x == 0 or x == 1:
        return False
    elif x % 2 == 0 and x != 2:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        z = 1
        y = 2*z + 1
        while y < x:
            if x % y == 0:
                return False
                break
            else:
                z = z + 1
                y = 2*z + 1
        if x == y:
            return True

def lista_primos(n):
    lista = [0]*n
    i = 0
    j = 0
    while j<n :
        if eh_primo(i):
            lista[j]=i
            j = j + 1
        i = i + 1
    return lista