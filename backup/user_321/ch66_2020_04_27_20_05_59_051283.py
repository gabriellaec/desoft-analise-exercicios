def lista_sufixos(s):
    l = []
    for i in range(len(s)):
        l.append(s[i:])
    return l