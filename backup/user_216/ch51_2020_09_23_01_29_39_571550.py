
def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d < n:
            if n % d == 0:
                return False
            else:
                d += 1
        while d >= n:
            return True

def primos_entre(a,b):
    lista = []
    i = a
    while i <= b:
        if i < 0:
            i +=
        elif eh_primo(i):
            lista.append(i)
            i += 1
    return lista