def estritamente_crescente(lista):
    l = []
    s = 0
    for x in lista:
        if x > s:
            l.append(x)
            s = x
    return l