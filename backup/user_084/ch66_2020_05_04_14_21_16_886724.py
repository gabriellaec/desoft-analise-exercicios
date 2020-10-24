def lista_sufixos(x):
    l=[]
    for i in range(len(x)):
        l.append(x[i:])
    return l