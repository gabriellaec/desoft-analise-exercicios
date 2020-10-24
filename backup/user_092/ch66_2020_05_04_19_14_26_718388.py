def lista_sufixos(x):
    L =[]
    i = 0
    while(i<len(x)):
        L.append(x[i:len(x)])
        i += 1
    return(L)