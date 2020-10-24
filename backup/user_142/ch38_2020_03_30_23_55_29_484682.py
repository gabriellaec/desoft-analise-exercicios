def quantos_uns(n):
    i = 0
    contador = 0
    n = str(n)
    while i < len(n):
        if n[i] == '1':
            contador = contador + 1
            i = i + 1
        else:
            i = i + 1
    return contador