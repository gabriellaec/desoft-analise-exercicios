def verifica_progressao(x):
    if len(x)<3:
        return "NA"
    else:
        if x[1]-x[0]==x[2]-x[1]:
            return "PA"
        elif x[1]/x[0]==x[2]/x[1]:
            return "PG"
        else:
            return "AG"