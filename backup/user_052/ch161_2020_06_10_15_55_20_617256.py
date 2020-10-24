def PiWallis (n):
    i = 1
    r = 2
    lista = []
    while r <= n:
        lista.append(r)
        lista.append(r)
        r += 2
    return lista
    r = 0
    while i <= n+1:
        soma *= lista[r]/i
        i += 2
        r += 1
        soma *= lista[r]/i
        i += 0
        r += 1
        soma*= lista[r]/i
        i += 2
        r += 1
        soma*= lista[r]/i
        i += 0
        r += 1
    return soma