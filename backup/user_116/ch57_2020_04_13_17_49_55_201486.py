def verifica_progressao(x):
    r1=x[1]-x[0]
    v1=x[2]-x[1]
    r2=x[1]/x[0]
    v2=x[2]/x[1]
    if r1==v1 and r2==v2:
        return "AG"
    if r1==v1:
        return "PA"
    if r2==v2:
        return "PG"
    else:
        return "NA"