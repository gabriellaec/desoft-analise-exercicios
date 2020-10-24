def lista_sufixos(s):
    lista=[]
    for i in range(len(s)):
        lista.append(s[i:])
    return lista