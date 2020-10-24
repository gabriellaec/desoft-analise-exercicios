def  verifica_progressao(nume):
    PA = [nume[0]]
    PG = [nume[0]]
    ra = nume[1] - nume[0]
    if nume[0] == 0:
        rg = 0
    else:
        rg = nume[1]/nume[0]
    for i in range(len(nume)-1):
        PA += [PA[i] + ra]
        PG += [PG[i]*rg]    
    if PA == nume and PG == nume:
        return "AG"
    elif PA == nume:
        return "PA"
    elif PG == nume:
        return "PG"
    else:
        return "NA"