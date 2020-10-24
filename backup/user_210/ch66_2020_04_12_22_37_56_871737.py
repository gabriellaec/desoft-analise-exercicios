def lista_sufixos(s):
    lista = []
    print(s)
    s = s[::-1]
    for c in range(1,len(s)):
        lista.append(s[:c])
    return lista