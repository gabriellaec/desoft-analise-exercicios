def lista_sufixos(P):
    if len(P) == 0 or len(P)==1:
        return P
    A = []
    i = 0
    while i <= len(P):
        A.append(P[i:len(P)+1])
        i += 1
    return A