def lista_sufixos(x):
    lista_sufixo=[]
    for i in range(len(x)):
        lista_sufixo.append(x[i:])
    return lista_sufixo
