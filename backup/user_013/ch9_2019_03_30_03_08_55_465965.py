def lista_sufixos(P):
    A = []
    i = 0
    while i <= len(P):
        A.append(P[i:])
        i += 1
    