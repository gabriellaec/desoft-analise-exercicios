def lista_sufixos(P):
    if len(P) == 0 or len(P) == 1 or len(P) == "":
        return ""
    return P[len(P)-1], P[len(P)-2],P[len(P)-3]