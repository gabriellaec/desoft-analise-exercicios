def quantos_uns(numero):
    n = str(numero)
    i = 0
    contador = 0
    while i < len(n):
        if n[i] == 1:
            contador = contador + 1
        i += 1
    return contador