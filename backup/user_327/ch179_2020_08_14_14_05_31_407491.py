def posicoes_minusculas(s):
    c = 0
    l = []
    for i in s:
        if i.islower():
            l.append(c)
        c += 1
    return l
        