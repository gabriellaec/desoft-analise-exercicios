def aniversariantes_de_setembro(dicionario):
    desetembro={}
    for i in dicionario:
        for j in i.values:
            if j[3]==0 and j[4]==9:
                desetembro[i]=i.values
    return desetembro
            