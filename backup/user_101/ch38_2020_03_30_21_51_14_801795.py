def quantos_uns(n):
    contador = 0
    n_str = str(n)
    for e in n_str:
        if e == 1:
            contador += 1
    return contador