def lista_sufixos(x):
    lista=[]
    for el in range(0,len(x)):
        lista.append(x[el:])
    return lista
