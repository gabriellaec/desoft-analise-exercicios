def lista_caracteres(s):
    f = []
    for e in s:
        if e not in f:
            f.append(e)
    return f
