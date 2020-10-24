def lista_sufixos(s):
    lista=[]
    i=0
    for i in range(len(s)):
        lista.append(s[i:])
    return lista