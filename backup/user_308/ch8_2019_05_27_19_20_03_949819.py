def verifica_progressao(listeras):
    "AG"=True
    "PG"=True
    "PA"=True
    for e in lista:
        if listeras[e+1]/listeras[e]!=listeras[e+2]/listeras[e+1] and listeras[e+1]-listeras[e]!=listeras[e+2]-listeras[e+1]:
            "AG"=False
        if listeras[e+1]/listeras[e]!=listeras[e+2]/listeras[e+1]:
            "PG"=False
        if listeras[e+1]-listeras[e]!=listeras[e+2]-listeras[e+1]:
            "PA"=False
    if "AG"==True:
        return "AG"
    elif "PG"==True:
        return "PG"
    elif "PA"==True:
        return "PA"
    else:
        return "NA"