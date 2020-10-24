def eh_primo(n):
    lista = []
    p = 3
    while p < n:
        lista.append(n%p)
        p += 2
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif 0 in lista:
        return False
    else:
        return True