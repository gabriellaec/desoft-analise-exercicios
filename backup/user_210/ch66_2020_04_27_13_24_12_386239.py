def lista_sufixos(s):
    lista = []
    for c in range(0,len(s)):
        lista.append(s[c:])
    return lista    