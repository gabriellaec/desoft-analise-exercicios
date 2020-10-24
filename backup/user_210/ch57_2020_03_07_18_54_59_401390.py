def verifica_progressao(l):
    if l[1]/l[0] == l[2]/l[1] and l[1]-l[0]==l[2]-l[1]:
        return "AG"
    elif l[1]/l[0] == l[2]/l[1]:
        return "PG"
    return "PA"