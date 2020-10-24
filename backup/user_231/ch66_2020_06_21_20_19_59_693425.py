def lista_sufixos(s):
    lista=[]
    lista.append(s)
    i=2
    for i in range(len(s)):
        lista.append(s[i:])
    return lista