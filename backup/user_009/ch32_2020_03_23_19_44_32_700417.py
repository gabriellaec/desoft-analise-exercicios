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
    listap = []
    contador = 0
    while len(listap) < n:
        eh_primo(i)
        contador += 1 
    return lista1