def eh_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x%2 == 0:
        return False
    else:
        n = 3
        while n < x:
            if x%n == 0:
                return False
            n += 2
        return True

def lista_primos(n):
    y = 2
    lista = []
    while y < n:
        if eh_primo(y) == True:
            lista.append(y)

        y += 1
    return lista