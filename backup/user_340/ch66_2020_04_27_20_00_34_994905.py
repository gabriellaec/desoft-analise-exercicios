def lista_sufixos(string):
    lista=[]
    i=len(string)
    while i>=1:
        lista.append(string[i-len(string):])
    return lista