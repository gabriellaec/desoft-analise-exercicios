def verifica_progressao(p):
    a = 0
    if p[1]/p[0] == p[2]/p[1] and p[1]-p[0] == p[2]-p[1]:
        a = "AG"
    elif p[1]/p[0] == p[2]/p[1] and p[1]-p[0] != p[2]-p[1]:
        a = "PG"
    else:
        a = "PA"

    return a