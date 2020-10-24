def lista_sufixos(s):
    l = []
    for i, e in enumerate(s):
        su = s[i:]
        l.append(su)
    return l