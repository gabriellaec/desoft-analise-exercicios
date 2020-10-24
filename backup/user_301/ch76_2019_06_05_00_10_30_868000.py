def aniversariantes_de_setembro(dc):
    dc2=dict()
    for k in dc.keys():
        if (dc[k][3:5])=="09":
            dc2[k]=dc[k]
    return dc2