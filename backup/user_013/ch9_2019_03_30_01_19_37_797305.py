def lista_sufixos(P):
    if len(P) == 0:
        return ""
    return P[len(P)-1], P[len(P)-2],P[len(P)-3]