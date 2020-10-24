def verifica_progressao (nros):
    print (nros)
    if nros == []:
        return "NA"
    if len(nros)<3:
        return "NA"

    for i in nros:
        if i == 0:
            return "NA"
    r = nros[1]-nros[0]
    q = nros [1]/nros[0]
    PA = True
    PG = True
    for i in range(len(nros)-1):
        if r ≠ nros[i+1]-nros[i]:
            PA = False
    for i in range(len(nros)-1):
        if q ≠ nros [i+1]/nros[i]:
            PG = False
    if PG == True and PA == True:
        return "AG"
    if PG== True:
        return "PG"
    if PA==True:
        return "PA"
    else:
        return "NA"