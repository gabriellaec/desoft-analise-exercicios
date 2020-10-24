def interseccao_chaves(D,C):
    L=D.keys()
    M=C.keys()
    P=[]
    for c in L:
        if c in M:
            P.append(c)
    return P
