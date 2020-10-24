def lista_sufixos(P):
    #Lista de sufixos
    L = [0]*len(P)
    for a in range(0,len(P)):
        L[a] = P[a]
    return L