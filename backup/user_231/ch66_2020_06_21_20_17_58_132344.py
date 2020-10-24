def lista_sufixos(s):
    lista=[]
    lista.append(s)
    i=0
    for i in range(len(s)):
        del s[0]
        lista.append(s)
    return lista