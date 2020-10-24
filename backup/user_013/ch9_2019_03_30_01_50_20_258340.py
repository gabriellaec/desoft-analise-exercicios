def lista_sufixos(P):
    L = [0]*len(P)
    if len(P) == 1:
        L[0] = P
        return L
    else:
        for a in range(0,len(P)):
            L[a] = P[a]
    return L