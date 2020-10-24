def verifica_progressao(x):
    if len(x)<3:
        return "NA"
    else:
        for i in x:
            if x[i+1]-x[i]==x[i+2]-x[i+1]:
                return "PA"
            elif x[i+1]/x[i]==x[i+2]/x[i+1]:
                return "PG"
            else:
                return "AG"