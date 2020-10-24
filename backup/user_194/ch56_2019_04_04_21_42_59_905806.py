def calcula_nota_fiscal(p,q):
    nota = 0
    i = 0
    while i < len(p):
        nota += p[i] * q[i]
        i += 1
    return nota