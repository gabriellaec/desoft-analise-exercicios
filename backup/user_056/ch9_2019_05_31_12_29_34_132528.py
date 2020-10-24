def lista_sufixos(x):
    lista_sufixo=[]
    for i in range(len(x)):
        lista_sufixo.append(lista_sufixo.join()+x[len(x)-1-i])
    return lista_sufixo