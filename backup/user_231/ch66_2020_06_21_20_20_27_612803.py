def lista_sufixos(s):
    lista=[]
    i=1
    for i in range(len(s)):
        lista.append(s[i:])
    return lista