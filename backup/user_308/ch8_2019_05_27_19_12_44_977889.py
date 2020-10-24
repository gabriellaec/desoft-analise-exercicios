def verifica_progressao(listeras):
    if listeras[1]/listeras[0]==listeras[2]/listeras[1] and listeras[1]-listeras[0]==listeras[2]-listeras[1]:
        return "AG"
    elif listeras[1]/listeras[0]==listeras[2]/listeras[1]:
        return "PG"
    elif listeras[1]-listeras[0]==listeras[2]-listeras[1]:
        return "PA"
    else:
        return "NA"