def verifica_progressao(l):
    if (l[0]+l[2])/2==l[1]:
        return "PA"
    elif l[2]/l[1]==l[1]:
        return "PG"
    elif (l[0]+l[2])/2==l[1] and l[2]/l[1]==l[1]:
        return "AG"
    else:
        return "NA"