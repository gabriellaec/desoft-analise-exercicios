def lista_sufixos (string):
    lista=[]
    for i in range(0,len(string)):
        lista.append(string[i:])
    return lista