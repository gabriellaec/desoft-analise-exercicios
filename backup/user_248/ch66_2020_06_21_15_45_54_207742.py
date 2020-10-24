def lista_sufixos(x):
    lista=[]
    for i in range(len(x)):
        lista.append(x[i]::len(x))
    return lista
        