def quantos_uns(n):
    p = str(n)
    contador = 0
    Uns = 0
    while contador < len(p):
        if p[contador] == "1":
            contador += 1
            Uns += 1
        else:
            contador += 1
    return Uns
