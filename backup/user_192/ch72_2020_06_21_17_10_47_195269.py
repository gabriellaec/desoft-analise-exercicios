def lista_caracteres(txt):
    a = []
    for i in range(len(txt)):
        if not txt[i] in a:
            a.append(txt[i])
    return a
        