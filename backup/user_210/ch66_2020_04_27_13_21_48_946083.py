def lista_sufixos(s):
    lista = []
    s = s[::-1]
    for c in range(0,len(s)):
        lista.append(s[:c])
    return lista