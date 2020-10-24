def interseccao_valores(D,C):
    L=D.values()
    M=C.values()
    P=[]
    for c in L:
        if c in M:
            P.append(c)
    return P